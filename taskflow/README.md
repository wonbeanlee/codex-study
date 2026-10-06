# Taskflow 작업 기록

AI가 우선순위를 추천하는 할 일 관리 SaaS를 만드는 프로젝트입니다. 현재는 Python `Todo` 클래스와 테스트까지 구현했으며, AI 추천, API, DB, 웹 화면은 아직 구현하지 않았습니다.

## 1. Codex에 요청한 명령어(프롬프트)

### 기여 가이드 생성

```text
Generate a file named AGENTS.md that serves as a contributor guide for this repository.
Before writing, check whether AGENTS.md already exists in the current working directory. If it does, do not overwrite or modify it.
```

최초 요청의 핵심 발췌입니다. 저장소 구조, 개발 명령어, 코드 스타일, 테스트, 커밋 및 PR 규칙을 담은 200~400단어 분량의 가이드를 요청했습니다. 기존 파일이 없는 것을 확인한 뒤 생성했습니다.

### Taskflow 전용 규칙으로 교체

```text
AGENTS.md를 아래 내용으로 작성해줘:
```

이 요청과 함께 전달한 프로젝트 규칙으로 기존 문서를 교체했습니다. 전체 규칙은 [AGENTS.md](AGENTS.md)에 원문 그대로 보관합니다.

- 계획한 기술: Python + FastAPI, SQLite(개발) → PostgreSQL(운영), HTML/CSS와 JavaScript.
- 기능을 작게 수직 분해하고, 코드 수정 후 `pytest` 실행 및 새 기능 테스트 작성.
- PEP8과 black 사용, 영어 식별자와 한국어 주석 작성.
- 새 패키지 추가 전 확인, `requirements.txt`로 의존성 관리.
- 비밀값은 환경 변수로 관리하고, 데이터 삭제·마이그레이션 전 사람의 확인 필요.

### 적용된 지침 확인

```text
현재 적용된 프로젝트 지시(instructions)를 요약해서 알려줘
```

프로젝트 지침을 요약했습니다. 원문의 `HTML/CCS`, `RESTfulgkrp`, `/todos/{id}}`는 오타로 보인다고 설명했으며 파일은 수정하지 않았습니다.

### Todo 클래스 구현

```text
todo를 표현하는 간단한 파이썬 클래스를 todo.py에 만들어줘
```

표준 라이브러리 `dataclasses`로 제목과 완료 여부를 표현하는 클래스를 작성했습니다. 완료 처리 메서드와 테스트도 추가했으며 새 패키지는 설치하지 않았습니다.

### 작업 기록 및 커밋

```text
이 taskflow도 README.md 로 내가 준 명령어들을 정리하고, git commmit 해줘
```

요청과 구현 결과를 이 README에 정리하고 Taskflow 파일을 Git 커밋 대상으로 준비했습니다.

## 2. 파일 구성

```text
taskflow/
├── .gitignore    # Python 및 pytest 캐시 제외
├── AGENTS.md     # 프로젝트 작업 규칙
├── README.md     # 요청문과 작업 기록
├── todo.py       # Todo 데이터 클래스
└── test_todo.py  # Todo 동작 테스트
```

`taskflow/`는 상위 `codex-study` Git 저장소에 포함됩니다. 아직 FastAPI 앱, DB, 의존성 파일은 없습니다.

## 3. 사용 예시

```python
from todo import Todo

todo = Todo(title="장보기")
print(todo.completed)  # False

todo.complete()
print(todo.completed)  # True
```

`title`은 필수이며 `completed`는 기본값이 `False`입니다. `Todo(title="장보기", completed=True)`로 완료 상태에서 생성할 수도 있습니다.

## 4. 테스트와 Git 명령어

`taskflow/` 디렉터리에서 실행합니다. 테스트에는 환경에 설치된 `pytest`가 필요합니다.

```bash
python3 -m pytest -q
git status --short
git add -- .gitignore AGENTS.md README.md todo.py test_todo.py
git diff --cached --stat
git diff --cached --check
git commit -m "Add Taskflow todo model and document workflow"
```

테스트는 기본 생성 상태, 완료 상태로 생성, 반복 완료 처리와 다른 할 일의 상태 독립성을 검증합니다. 구현 후 실행 결과는 **3 passed**입니다.
