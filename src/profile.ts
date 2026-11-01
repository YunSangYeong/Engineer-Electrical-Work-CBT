// Q-Net 접근이 차단되어 공식 문서 대조는 미완료. docs/verification.md 참조.
export const PROFILE = {
  name: "전기공사기사", rulesVerificationStatus: "pending",
  subjects: ["전기응용 및 공사재료", "전력공학", "전기기기", "회로이론 및 제어공학", "전기설비기술기준"] as const,
  questionCount: 100, questionsPerSubject: 20, durationMinutes: 150,
  choiceCount: 4, passScore: 60, subjectCutoff: 40,
} as const;
