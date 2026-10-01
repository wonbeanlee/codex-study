# 2026-09-30 Codex 작업 기록

Codex에 자연어로 요청해 Python 인사 프로그램을 만들고, 한글 입력 환경을 설정하고, Git과 GitHub 연결을 실습했습니다. 이 문서는 당시 `26.09.30` 폴더에서 진행한 대화 기록을 바탕으로 작성했습니다. 입력문의 오탈자와 줄바꿈은 읽기 쉽게 정리했으며, 인증 정보는 제외했습니다.

## 1. Codex에 입력한 요청과 작업 결과

### Python 인사 프로그램 만들기

```text
greet.py 파일을 만들어줘.
이름을 입력받아서 "안녕하세요, OOO!"이라고 출력하는 파이썬 프로그램이야.
초보자가 이해하기 쉽게 주석도 달아줘.
```

`greet.py`를 만들고 입력, 변수, 출력의 역할을 주석으로 설명했습니다.

### 빈 이름 처리하기

```text
greet.py를 수정해서 이름이 비어 있으면 "이름을 입력해주세요"라고 안내하고
```

위 요청에 따라 빈 입력이나 공백만 입력하면 안내 문구를 출력하고 다시 입력받도록 수정했습니다. `strip()`으로 양끝 공백을 제거하고, `while True`와 `break`로 입력 반복을 제어합니다.

### 코드 설명 요청하기

```text
greet.py가 무슨 일을 하는지 한 줄로 설명해줘.
```

당시에는 이름이 비어 있으면 다시 입력받고, 이름이 있으면 한국어 인사말을 출력하는 프로그램이라고 설명했습니다.

### 영어 인사말 추가하기

```text
greet.py에서 인사말을 영어로도 함께 출력하도록 한 줄 추가해줘.
```

한국어 인사말 다음에 `Hello, 이름!`도 출력하도록 수정했습니다.

### 함수를 다른 파일로 분리하기

```text
utils.py 파일을 새로 만들어서 인사말을 만드는 함수를 옮기고,
greet.py에서는 그 함수를 가져다 쓰도록 리팩터링 해줘.
```

대화에서는 두 문장으로 나누어 입력했습니다. `utils.py`에 `make_greetings(name)` 함수를 만들고, `greet.py`에서 가져다 쓰도록 정리했습니다.

```python
from utils import make_greetings

korean_greeting, english_greeting = make_greetings(name)
print(korean_greeting)
print(english_greeting)
```

`utils.py`는 두 인사말을 만들어 반환하고, `greet.py`는 이름 입력과 빈 입력 확인, 화면 출력을 담당합니다.

### 한글 입력 문제 해결하기

```text
Again not working hangul
```

```text
i want to user ibus hangul forever but it still not working
can you check it in my terminal?
```

```text
지금 한/영 변환을 shift+space로 하고 있는데,
한/영 키로도 변환할 수 있게 추가해줘.
```

IBus Hangul의 활성 입력기와 저장된 설정을 확인하고, 한글 입력기를 유지하도록 설정했습니다. 기존 `Shift+Space`를 유지하면서 오른쪽 Alt 위치의 한/영 키도 전환키로 매핑했습니다. 이후 사용자가 “좋아 잘 되는거 같아”라고 응답했습니다. 재부팅 후 동작까지 확인한 기록은 없습니다.

이 작업은 로컬 데스크톱 설정 변경이며, 해당 설정 파일은 이 폴더의 소스에 포함되어 있지 않습니다.

### 파일 목록 확인하기

```text
현재 폴더의 파일 목록을 보여줘.
```

당시 작성한 `greet.py`와 `utils.py`를 확인했습니다.

### requests의 의미와 설치 요청하기

```text
requests 라이브러리의 의미를 알려주고 설치해줘.
```

웹사이트나 API에 요청을 보내고 응답을 받는 Python 라이브러리라는 설명을 받았습니다. 당시 기본 Python에 `pip`가 없어 프로젝트의 `.venv`에 설치 도구를 준비하고 `requests`를 설치했으며, 불러오기도 확인했습니다.

현재 인사 프로그램은 `requests`를 사용하지 않습니다. `.venv`는 Git 추적 대상에서 제외되어 있습니다.

### 변경 내역 확인하기

```text
/diff greet.py
```

당시 폴더가 아직 Git 저장소가 아니어서 Git diff 대신 대화 기록을 기준으로 함수 분리 전후를 설명했습니다. 이후 Git을 함께 사용하는 실습으로 이어졌습니다.

### Git 초기화와 GitHub 연결하기

```text
git 을 같이 쓰고 싶어
```

폴더를 Git 저장소로 초기화하고 `.gitignore`에 가상환경과 Python 캐시 제외 설정을 추가했습니다. 작성자 설정 후 첫 로컬 커밋 `973abe0`을 만들었습니다.

저장소 주소를 전달한 뒤, 다음과 같은 초기 업로드 명령도 입력했습니다.

```bash
echo "# codex-study" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/wonbeanlee/codex-study.git
git push -u origin main
```

위 블록은 당시 입력한 내용입니다. 이미 초기화와 커밋이 되어 있어 Codex는 상태를 확인하고 원격 주소를 변경했습니다. 기존 원격 README를 병합한 기록도 있으나, 당시 Codex의 업로드 시도는 GitHub 인증 정보가 없어 실패했습니다.

## 2. 파일 구성

```text
26.09.30/
├── .gitignore  # .venv와 Python 캐시 제외
├── README.md   # Codex 입력과 실습 기록
├── greet.py    # 이름 입력, 빈 입력 확인, 인사말 출력
└── utils.py    # 한국어·영어 인사말 생성 함수
```

## 3. 프로그램 실행 방법

저장소 루트에서 실행합니다. 이 프로그램에는 Python 3만 필요합니다.

```bash
cd 26.09.30
python3 greet.py
```

예상 실행 예시:

```text
이름을 입력하세요:
이름을 입력해주세요
이름을 입력하세요: 홍길동
안녕하세요, 홍길동!
Hello, 홍길동!
```

## 4. 이후 GitHub 폴더 문제 해결 (2026-10-01)

```text
지금 26.09.30 이 git repository에 안올라와 있어
폴더에 화살표 방향이 그려져 있는데,
https://github.com/wonbeanlee/codex-study/tree/main 확인하고 수정해줘
```

상위 저장소가 `26.09.30`을 실제 파일 대신 중첩 저장소의 커밋을 가리키는 Git 링크로 추적하고 있었습니다. 내부 Git 기록을 상위 `.git/26.09.30-git-backup`에 백업한 뒤 일반 폴더로 전환했습니다.

`.gitignore`, `README.md`, `greet.py`, `utils.py` 네 파일을 상위 저장소에 등록하고, 수정 커밋 `304a384`를 GitHub `main`에 푸시했습니다. 가상환경은 제외했습니다. 백업은 로컬에만 있으며 GitHub에는 업로드되지 않습니다.

## 5. 학습한 내용

- 자연어로 코드 생성, 수정, 설명을 요청하기
- `input()`, `strip()`, 반복문과 조건문으로 입력 처리하기
- 함수의 반환값과 `import`로 파일 사이의 역할 나누기
- 가상환경에 라이브러리를 설치하고 Git 추적에서 제외하기
- Git 초기화, 커밋, 원격 연결과 업로드의 차이 이해하기
- 날짜별 폴더 안에 별도 저장소를 만들면 상위 저장소에서 Git 링크로 등록될 수 있다는 점 확인하기

[GitHub에서 26.09.30 폴더 보기](https://github.com/wonbeanlee/codex-study/tree/main/26.09.30)
