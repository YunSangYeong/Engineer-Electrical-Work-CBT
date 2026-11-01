import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';
import { BASE_BANK as bank, SUBJECTS, createExam, grade, emptyStore, submitExam, answerExam, remainingSeconds, restoreStore, startPractice, nextPractice, checkPractice, importQuestions, fingerprint, validateQuestion, parseCsv } from '../src/model';
import { expandedEvaluators, expectedUnits } from './calculation-evaluators';
import { PROFILE } from '../src/profile';

describe('은행과 독립 역산 검증',()=>{
 it('기존 100문항 ID·내용·정답·해설·메타데이터 보존',()=>{expect(createHash('sha256').update(JSON.stringify(bank.slice(0,100))).digest('hex')).toBe('40039ba15548701fb3f20d9fbc20b61f319d64b4b1aef13be0a6344782438331');});
 it('각 유형은 서로 다른 조건 20개',()=>{for(const family of new Set(bank.map(q=>q.family))){const rows=bank.filter(q=>q.family===family);expect(rows).toHaveLength(20);expect(new Set(rows.map(q=>JSON.stringify(q.calculation?.values))).size).toBe(20);}});
 it('1000문항·50유형·과목별200개, ID/정규화 중복 없음',()=>{
  expect(bank).toHaveLength(1000); expect(1000-bank.length).toBe(0);
  expect(new Set(bank.map(q=>q.id)).size).toBe(1000);
  expect(new Set(bank.map(fingerprint)).size).toBe(1000);
  expect(new Set(bank.map(q=>q.family)).size).toBe(50);
  SUBJECTS.forEach(s=>expect(bank.filter(q=>q.subject===s)).toHaveLength(200));
 });
 for(const q of bank) it(q.id+' 조건·단위·정답의 독립 역산',()=>{
  expect(()=>validateQuestion(q)).not.toThrow();
  expect(q.type).toBe('original');expect(q.year).toBeNull();expect(q.session).toBeNull();
  const c=q.calculation!, [a,b]=c.values, answer=Number(q.choices[q.answer-1].split(' ')[0]);
  expect(answer).toBe(c.result);
  expect(c.unit).toBe(expectedUnits[c.kind]);
  if(c.kind==='illuminance') expect(answer*b).toBe(a);
  else if(c.kind==='lineLoss') expect(Math.sqrt(answer/b)).toBe(a);
  else if(c.kind==='slip') expect(a*(1-answer/100)).toBeCloseTo(b,8);
  else if(c.kind==='impedance') expect(answer**2-a**2).toBe(b**2);
  else if(c.kind==='protectiveDrop') expect(answer/a).toBe(b);
  else {
   const evaluator = expandedEvaluators[c.kind];
   if (!evaluator) throw Error('Unknown calculation: '+c.kind);
   const raw=evaluator(c.values);
   expect(Math.abs(answer-raw)).toBeLessThanOrEqual(0.005000001);
   expect(q.choices[q.answer-1].slice(q.choices[q.answer-1].indexOf(' ')+1)).toBe(c.unit);
  }
  expect(new Set(q.choices.map(Number.parseFloat)).size).toBe(4);
  expect(q.reviewNote).toContain('전문가');
 });
});
describe('시험·과락·시간·보존',()=>{
 it('100문항, 과목별20, 150분; 부족 은행 거부',()=>{
  const e=createExam(bank,'main',1000);expect(e.questions).toHaveLength(100);
  expect(e.deadline-e.startedAt).toBe(9000000);
  SUBJECTS.forEach(s=>expect(e.questions.filter(q=>q.subject===s)).toHaveLength(20));
  expect(()=>createExam(bank.filter(q=>q.subject!==SUBJECTS[0] || bank.filter(x=>x.subject===SUBJECTS[0]).slice(0,19).includes(q)),'main')).toThrow();
  expect(new Set(e.questions.map(q=>q.family)).size).toBe(50);
 });
 function scored(counts:number[]){const e=createExam(bank,'main');SUBJECTS.forEach((s,j)=>e.questions.filter(q=>q.subject===s).slice(0,counts[j]).forEach(q=>e.answers[q.id]=q.answer));return grade(e);}
 it('60점 및40점 경계는 합격, 평균/과락은 원값으로 판정',()=>{
  expect(scored([8,13,13,13,13]).passed).toBe(true);
  expect(scored([7,20,20,20,20]).passed).toBe(false);
  expect(scored([8,12,13,13,13]).passed).toBe(false);
  expect(scored([0,0,0,0,0]).unanswered).toBe(100);
 });
 it('즉시 답안 보존·만료 답안 차단·중복제출 차단·복원',()=>{
  const e=createExam(bank,'main',1000),q=e.questions[0];
  let s={...emptyStore(),exam:e};s=answerExam(s,q.id,q.answer,2000) as typeof s;
  expect(restoreStore(JSON.stringify(s)).exam?.answers[q.id]).toBe(q.answer);
  const done=answerExam(s,e.questions[1].id,1,e.deadline);
  expect(done.exam).toBeNull();expect(done.results[0].reason).toBe('timeout');
  expect(Object.keys(done.results[0].answers)).toHaveLength(1);
  expect(submitExam(done).results).toHaveLength(1);
  expect(remainingSeconds(e.deadline,e.deadline+1)).toBe(0);
  expect(()=>restoreStore('{broken')).toThrow();
 });
 it('자격증 설정은 공식 확인 미완료를 명시',()=>expect(PROFILE.rulesVerificationStatus).toBe('pending'));
});
describe('랜덤·검수대기·중복',()=>{
 it('순회 중 ID 중복 방지·한번만 채점·정답 재학습은 오답 제거',()=>{
  let p=startPractice(bank,'main'),seen=new Set<string>();
  for(let i=0;i<bank.length;i++){expect(seen.has(p.currentId)).toBe(false);seen.add(p.currentId);p=nextPractice(p,bank);}
  const q=bank.find(q=>q.id===p.currentId)!;
  const s={...emptyStore(),wrongIds:[q.id],practice:{...p,selected:q.answer}};
  const checked=checkPractice(s,bank);expect(checked.wrongIds).toEqual([]);
  expect(checkPractice(checked,bank).attempts).toHaveLength(1);
 });
 it('보기 재배치·본문 중복 제거 및 일괄 원자 검증·검수대기 강제',()=>{
  const q=bank[0];expect(importQuestions([{...q,id:'COPY',choices:[...q.choices].reverse()}],bank).duplicates).toBe(1);
  const added=importQuestions([{...q,id:'LOCAL',question:'새로운 질문'}],bank).added;
  expect(added[0].verificationStatus).toBe('pending');
  expect(()=>importQuestions([added[0],{}],bank)).toThrow('2번 문항');
  expect(()=>parseCsv('id,id\na,b')).toThrow();
 });
});
