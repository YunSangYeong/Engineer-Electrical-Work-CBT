"""Deterministic new exercises. No past questions or statutory limits are reproduced."""
import json,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
subjects=['전기응용 및 공사재료','전력공학','전기기기','회로이론 및 제어공학','전기설비기술기준']
bank=[]
for k,subject in enumerate(subjects):
 for n in range(1,21):
  if k==0:
   v=[100*n,5];r=20*n;unit='lx';topic='조명·평균 조도';kind='illuminance'
   text=f'면적 {v[1]} m²인 작업면에 광속 {v[0]} lm이 균일하게 입사한다. 평균 조도는? (손실은 이미 반영된 입사 광속이다.)'
   explanation=f'평균 조도는 작업면에 입사한 총 광속을 면적으로 나눈 값이다. E=Φ/A={v[0]}/{v[1]}={r} lx. 광원 자체의 광속과 입사 광속을 혼동하지 않는다.'
  elif k==1:
   v=[n+2,2];r=2*(n+2)**2;unit='W';topic='배전·저항 손실';kind='lineLoss'
   text=f'저항 {v[1]} Ω인 선로 도체 한 가닥에 실효값 {v[0]} A가 흐른다. 이 도체 한 가닥의 줄 손실 전력은? (왕복 두 가닥 합계가 아니다.)'
   explanation=f'도체의 유효전력 손실은 P=I²R이다. 실효값을 사용하므로 P={v[0]}²×{v[1]}={r} W. 제시된 저항은 도체 한 가닥의 전체 저항이므로 왕복 계수 2를 추가하지 않는다.'
  elif k==2:
   v=[1500,1500-15*n];r=n;unit='%';topic='유도전동기·슬립';kind='slip'
   text=f'유도전동기의 동기속도는 {v[0]} min⁻¹, 회전자 속도는 {v[1]} min⁻¹이다. 슬립의 백분율은?'
   explanation=f'슬립은 동기속도에 대한 속도 차의 비율이다. s=(Ns-N)/Ns×100=({v[0]}-{v[1]})/{v[0]}×100={r} %. 모터 운전이며 회전자 속도가 동기속도보다 낮다.'
  elif k==3:
   v=[3*n,4*n];r=5*n;unit='Ω';topic='교류·직렬 RL';kind='impedance'
   text=f'저항 {v[0]} Ω과 유도 리액턴스 {v[1]} Ω이 직렬 연결된 교류 회로이다. 임피던스 크기는?'
   explanation=f'직렬 RL 회로에서 Z=R+jX이므로 크기는 √(R²+X²)이다. |Z|=√({v[0]}²+{v[1]}²)={r} Ω. 저항과 리액턴스는 위상이 직교하므로 크기를 단순 합산하지 않는다.'
  else:
   v=[2*n,10];r=20*n;unit='mV';topic='보호도체·연속성 측정 기초';kind='protectiveDrop'
   text=f'보호도체 연속성의 기초 계산 연습이다. 시험 전류 {v[0]} A에서 도체 저항이 {v[1]} mΩ일 때 전압 강하는? (적합 여부나 법정 시험 전류를 묻는 문제가 아니다.)'
   explanation=f'옴의 법칙 U=IR을 적용한다. {v[1]} mΩ={v[1]/1000:g} Ω이므로 U={v[0]}×{v[1]/1000:g}={r/1000:g} V={r} mV. 이 계산만으로 보호도체의 법규 적합 판정을 할 수 없으며 법정 한계값을 제시하지 않는다.'
  choices=[f'{r} {unit}',f'{r*2} {unit}',f'{r*3} {unit}',f'{r*4} {unit}'];rotation=n%4
  choices=choices[rotation:]+choices[:rotation]
  bank.append(dict(id=f'EWC-{k+1}-{n:03}',subject=subject,topic=topic,question=text,choices=choices,answer=choices.index(f'{r} {unit}')+1,explanation=explanation,difficulty='하',year=None,session=None,type='original',sourceUrl='https://github.com/YunSangYeong/Engineer-Electrical-Work-CBT',verificationStatus='reviewed',reviewNote='AI 일반 전기 지식으로 신규 작성. 템플릿 조건·단위·해설을 내부 검토하고 독립 역산 테스트 수행. 외부 자료·공식 출제기준 대조 및 전문가 검수 미실시. 저장소는 작성 위치이며 외부 정답 증빙이 아님. 자체 제작 계산 조건 변형.',version='main',rights='자체 제작 · CC BY 4.0 · Engineer-Electrical-Work-CBT contributors 표시',family=f'EWC-F{k+1}',calculation=dict(kind=kind,values=v,result=r,unit=unit)))
from expanded_bank import additional_questions
bank.extend(additional_questions(subjects))
assert len(bank) == 1000
(ROOT/'src/data/questions-main.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
example={**bank[0],'id':'LOCAL-SAMPLE-001','question':bank[0]['question']+' [등록 양식 예제]','verificationStatus':'pending','reviewNote':'실제 사용 전 출처·권한·정답 확인 필요'}
(ROOT/'public/templates/questions.json').write_text(json.dumps([example],ensure_ascii=False,indent=2)+'\n')
row={k:v for k,v in example.items() if k not in ['choices','family','calculation']}
for i,c in enumerate(example['choices'],1):row[f'choice{i}']=c
with (ROOT/'public/templates/questions.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(row),lineterminator="\n");w.writeheader();w.writerow(row)
print(f'{len(bank)} exercises, 50 families, 20 conditions each; target shortfall {1000-len(bank)}')
