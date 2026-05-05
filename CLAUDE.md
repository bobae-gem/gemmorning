# gemmorning 채널

매일 아침 7시 업로드. 1분 이내 숏츠 영상.
하루를 시작하는 사람들에게 힐링과 에너지를 전달한다.
플랫폼: YouTube Shorts (우선 집중 · 틱톡·인스타는 추후 확장)

---

## 커뮤니케이션 원칙

### 사용자 → 채널 소통 방식
- 사용자가 **지시하거나 질문**할 때 → **총괄매니저**가 첫 번째로 받는다
- 총괄매니저가 내용을 판단하여 해당 팀/담당자에게 전달한다
- 사용자가 **팀원에게 직접 지시**한 경우 → 팀원은 작업 후 반드시 **총괄매니저에게 보고**한다
- 총괄매니저는 항상 모든 업무 내용을 파악하고 있어야 한다

### 작업 시작 전 필수 규칙
- **누구든 작업 시작 전** → `shared/channel-rules.md` 반드시 참조
- 규칙 확인 없이 작업 시작 금지

---

## 조직 구조

```
사용자
  ↕ (지시·질문 / 보고)
총괄매니저 (agents/manager.md)
  ├── 서치팀
  │   ├── 리서치사 (agents/researcher.md)
  │   └── 작가 (agents/writer.md)
  ├── 데이터분석팀
  │   └── 채널 분석가 (agents/data-analyst.md)
  └── SNS팀
      ├── 업로드 담당 (agents/uploader.md)
      └── 콘텐츠 최적화 전략가 (agents/optimizer.md)
```

---

## 에이전트 목록

| 파일 | 역할 | 소속 |
|------|------|------|
| `agents/manager.md` | 총괄 관리·지시 배분·보고 수합 | 총괄 |
| `agents/searcher.md` | YouTube·네이버·구글 소재 발굴 (3개) | 서치팀 |
| `agents/search-writer.md` | 소재 3개 브랜드 초안 작성 | 서치팀 |
| `agents/researcher.md` | 초안 3개 평가 후 최종 1위 선정 | 서치팀 |
| `agents/writer.md` | 선정된 소재로 대본 작성 | 서치팀 |
| `agents/data-analyst.md` | 전 채널 데이터 분석·리포트 | 데이터분석팀 |
| `agents/optimizer.md` | 제목·태그·내용 최적화 전략 | SNS팀 |
| `agents/uploader.md` | 플랫폼 업로드·댓글 관리 | SNS팀 |

---

## 워크플로우

### 일반 흐름
1. 사용자 지시/질문 → `manager` 수신
2. `manager` → 해당 팀에 지시 (channel-rules.md 참조 명시)
3. 팀원 작업 완료 → `manager`에게 보고
4. `manager` → 사용자에게 최종 보고

### 콘텐츠 제작 흐름
1. `searcher` → YouTube·네이버·구글 소재 3개 발굴 (마감 06:00)
2. `search-writer` → 소재 3개 gemmorning 브랜드 초안 작성
3. `researcher` → 초안 3개 평가 → 최종 1위 선정
4. `writer` → 선정된 소재로 대본 완성
5. `optimizer` → 제목·태그 제안
6. `manager` → 최종 승인
7. `uploader` → 07:00 YouTube 업로드

### 일일 리포트 흐름 (새벽 04:00)
1. `data-analyst` → 데이터 수집 (전일 04:00~당일 04:00)
2. `optimizer` → 최적화 인사이트
3. `manager` → 아래 경로에 보고서 저장 → 팅 자동 수신
   - 저장 경로: `C:\Users\user\Desktop\클로드\practice\dashboard\output\dolmorning_manager_report.json`

---

## 공통 규칙

`shared/channel-rules.md` 참조
