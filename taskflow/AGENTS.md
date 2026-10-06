# Taskflow 프로젝트 규칙

## 프로젝트 개요
- AI가 우선순위를 추천해주는 할 일 관리 SaaS
- 백엔드 : Python + FastAPI, DB:SQLite(개발) -> PostgreSQL(운영)
- 프런트엔드 : HTML/CCS + 약간의 Javascript

## 작업 방식
- 기능은 작게 쪼개서 하나씩 완성한다(수직 분해).
- 코드를 수정하면 항상 `pytest`로 테스트를 실행한다.
- 새 기능에는 반드시 테스트를 함께 작성한다.

## 코드 스타일
- Python은 PEP8, 포매터는 black.
- 함수/변수명은 영어, 주석은 한국어.
- API 경로는 RESTfulgkrp(`/todos`, `/todos/{id}}`).

## 의존성 
- 새 패키지 추가 전에 먼저 물어본다.
- 의존성은 requirements.txt로 관리

## 보안/금지
- 비밀키, 토큰은 코드에 넣지 않고 환경 변수로 관리한다.
- 데이터 삭제/마이그레이션은 사람 확인 후 실행한다.
