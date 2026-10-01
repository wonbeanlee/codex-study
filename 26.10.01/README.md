# 2026-10-01 Codex 작업 기록

Codex에 자연어로 요청해 자기소개 페이지를 만들고, 디자인을 수정한 뒤 GitHub에 업로드한 과정을 정리했습니다. 아래 요청문은 대화에서 사용한 내용을 읽기 쉽게 정리한 것입니다.

## 1. Codex에 요청한 명령어(프롬프트)

### HTML 페이지 생성

```text
index.html 한 페이지를 만들어줘.
```

처음에는 한국어 랜딩 페이지를 만들었습니다.

### 자기소개 페이지로 변경

```text
index.html 한 파일을 만들어줘.
내 소개 페이지: 이름, 한 줄 소개, "연락하기" 버튼.
HTML과 CSS는 한 파일 안에 넣고, 별도 파일 없이 만들어줘.
모바일에서도 잘 보이게 반응형으로 만들어줘.
```

이름, 한 줄 소개, 이메일 연락 버튼이 있는 자기소개 페이지로 변경했습니다. CSS는 HTML의 `<style>` 안에 넣었습니다.

### 디자인 개선 및 개인정보 반영

```text
이 페이지의 디자인을 개선해줘.
배경은 단색 말고 부드러운 그라데이션으로 표현하고,
표현력 있는 폰트와 버튼 hover 애니메이션을 적용해줘.
보라색과 흰색 조합은 피하고 청록 계열로,
전체적으로 의도적으로 세련된 느낌으로 만들어줘.
이름은 이원빈, 이메일은 lwb1217@gmail.com.
```

- 청록색 그라데이션 배경과 민트색 포인트 적용
- 이름에 명조체, 영문 이름에 세리프 이탤릭체 적용
- 버튼에 떠오르는 효과와 화살표 이동 애니메이션 적용
- 모바일 레이아웃과 키보드 포커스 표시 적용
- 기기의 동작 줄이기 설정에 따라 버튼 애니메이션 비활성화
- 연락 버튼을 `mailto:lwb1217@gmail.com`에 연결

폰트는 기기에 설치된 글꼴을 사용하므로 운영체제에 따라 모양이 달라질 수 있습니다.

### GitHub 업로드

```text
26.10.01 디렉토리를 나의 git repository에 올려줘.
```

연결된 `wonbeanlee/codex-study` 저장소의 `main` 브랜치에 폴더를 커밋하고 업로드했습니다. Python 캐시는 `.gitignore`로 제외했습니다.

### 작업 기록 작성

```text
작업한 Codex의 명령어도 정리해서
README.md로 26.10.01에 만들어서 Git에 올려줘.
```

이 문서를 작성하고 같은 저장소에 업로드하는 요청입니다.

## 2. 파일 구성

```text
26.10.01/
├── .gitignore        # Python 캐시 제외 설정
├── README.md         # 요청문과 작업 기록
├── index.html        # HTML과 CSS가 포함된 자기소개 페이지
├── calculator.py     # 폴더에 있던 사칙연산 계산기
└── test_calculator.py # 계산기 pytest 테스트
```

계산기 파일도 폴더 업로드에 함께 포함했습니다. 이 문서에서 정리한 대화에는 계산기 생성 요청이 포함되어 있지 않습니다.

## 3. 페이지 실행

`index.html`을 브라우저에서 열면 됩니다. 별도의 설치나 빌드 과정은 없습니다.

**연락하기** 버튼은 기기에 설정된 이메일 앱을 엽니다. 웹 페이지에서 이메일을 직접 전송하는 기능은 아닙니다.

## 4. 사용한 주요 터미널 명령어

다음 명령어는 `codex-study/26.10.01` 폴더에서 실행하는 기준입니다.

### 저장소와 파일 확인

```bash
git status --short
git rev-parse --show-toplevel
git remote -v
git branch --show-current
git log -2 --oneline
rg --files --hidden -g '!.git' -g '!node_modules'
cat index.html
```

각각 변경 사항, 저장소 경로, 원격 저장소, 현재 브랜치, 최근 커밋, 파일 목록, HTML 내용을 확인하는 명령어입니다.

### 소스 파일 커밋 및 업로드

```bash
git add -- .gitignore index.html calculator.py test_calculator.py
git diff --cached --stat
git diff --cached --check
git commit -m "Add October 1 profile page and calculator exercises"
git push origin main
```

스테이징된 변경 목록과 공백 오류를 확인한 뒤 커밋하고 업로드했습니다. `git diff --cached --check`는 브라우저 동작이나 Python 테스트를 검증하는 명령어는 아닙니다.

최초 폴더 업로드 커밋: `f45f5fe`.

### README 커밋 및 업로드

```bash
git add -- README.md
git diff --cached --check
git commit -m "Document October 1 Codex prompts and workflow"
git push origin main
```

## 5. 저장소

[GitHub에서 26.10.01 폴더 보기](https://github.com/wonbeanlee/codex-study/tree/main/26.10.01)

GitHub 저장소 업로드까지 진행했으며, 웹 사이트 배포는 별도로 설정하지 않았습니다.
