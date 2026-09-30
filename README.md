# codex-study

> Ubuntu에서 Codex와 함께 배우는 RTL 설계 · SystemVerilog 검증 · 개발 자동화

실습 코드를 직접 실행하고 결과를 확인하며, 날짜별로 문제 해결 과정을 기록하는 개인 학습 저장소입니다.

## 🎯 학습 목표

- Linux 터미널과 Git으로 개발 환경 관리하기
- Codex를 활용해 코드 분석, 테스트벤치 작성, 오류 수정하기
- Vivado/XSim으로 Verilog·SystemVerilog 동작 검증하기
- 실행 명령과 예상 결과를 남겨 다시 재현할 수 있는 실습 만들기

## 🛠️ 개발 환경

| 구분 | 구성 |
| --- | --- |
| 가상화 | VMware |
| 운영체제 | Ubuntu 24.04 계열, x86_64 |
| 편집기 | VS Code |
| AI 개발 도구 | Codex CLI |
| RTL 설계·시뮬레이션 | AMD Vivado 2026.1 / XSim |
| 버전 관리 | Git / GitHub |

실제 도구 실행 여부와 버전은 각 날짜의 실습 기록에 남깁니다. 이 표는 모든 기능의 검증 완료를 의미하지 않습니다.

## 📚 학습 기록

| 날짜 | 주제 | 기록 |
| --- | --- | --- |
| 2026-09-30 | Ubuntu 개발 환경 및 GitHub 연결 | [26.09.30 폴더](./26.09.30/) |

새 실습은 `26.10.01/README.md`처럼 날짜별 폴더에 추가합니다. 루트 README는 전체 안내, 날짜별 README는 실습 상세 기록으로 사용합니다.

## 📁 권장 폴더 구성

다음은 확장할 때 사용할 예시입니다. README만 추가한다고 아래 파일들이 자동으로 생성되지는 않습니다.

| 경로 | 내용 |
| --- | --- |
| `README.md` | 저장소 안내와 학습 목차 |
| `26.09.30/README.md` | 해당 날짜의 목표·과정·결과 |
| `26.09.30/rtl/` | RTL 설계 소스 |
| `26.09.30/tb/` | SystemVerilog 테스트벤치 |
| `26.09.30/scripts/` | Shell·Tcl 실행 스크립트 |
| `26.09.30/sim/` | 로컬 시뮬레이션 결과물 |

## 🚀 Ubuntu에서 시작하기

이미 저장소가 있는 경우, 로컬 변경을 먼저 확인하고 최신 내용을 가져옵니다.

```bash
cd ~/projects/codex-study
git status
git pull --ff-only
code README.md
```

로컬 수정이 있으면 커밋하거나 보관한 뒤 pull합니다. VS Code에서 `Ctrl + Shift + V`를 누르면 Markdown 미리보기를 볼 수 있습니다.

처음 받는 PC에서는 GitHub SSH 인증을 설정한 뒤 실행합니다.

```bash
mkdir -p ~/projects
cd ~/projects
git clone git@github.com:wonbeanlee/codex-study.git
cd codex-study
code .
```

## 🤖 Codex 활용 예시

프로젝트 폴더에서 실행합니다.

```bash
cd ~/projects/codex-study
codex
```

### 1. 현재 환경 파악

> 현재 저장소 구조와 README를 읽고, 설치된 xvlog·xelab·xsim 경로를 확인해줘. 파일을 수정하기 전에 확인 결과와 다음 실습을 제안해줘.

### 2. RTL과 테스트벤치 작성

> 26.09.30 폴더에 8비트 동기식 카운터를 작성해줘. active-low 동기 리셋과 enable을 포함하고, 테스트벤치에서 리셋·증가·정지·오버플로를 예상값과 비교해줘. XSim 실행 스크립트와 timeout을 넣고 실제 실행 여부를 보고해줘.

### 3. 오류 분석

> 시뮬레이션 로그의 첫 번째 오류부터 원인을 분석해줘. 설계 문제와 테스트벤치 문제를 구분하고, 최소 수정 후 같은 테스트를 다시 실행해줘. 검증하지 못한 부분은 명시해줘.

### 4. 학습 기록 작성

> 오늘 변경한 코드와 실제 실행 결과를 바탕으로 날짜별 README를 정리해줘. 목적, 환경, 명령어, 예상 결과, 실제 결과, 해결한 문제, 다음 할 일을 포함해줘.

## 🔬 XSim 실행 예시

아래 명령은 `26.09.30/rtl/counter.sv`와 `26.09.30/tb/tb_counter.sv`를 작성한 뒤 사용하는 예시입니다. 테스트벤치 최상위 모듈은 `tb_counter`이며, 완료 시 `$finish`를 호출해야 합니다.

먼저 실제 설치 경로의 환경 파일을 불러옵니다.

```bash
source "$HOME/tools/amd/2026.1/Vivado/settings64.sh"
command -v xvlog
command -v xelab
command -v xsim
```

```bash
cd ~/projects/codex-study/26.09.30
mkdir -p sim
cd sim

xvlog -sv ../rtl/counter.sv ../tb/tb_counter.sv
xelab work.tb_counter -debug typical -s counter_sim
xsim counter_sim -runall
```

각 단계가 성공했는지 확인하고 다음 단계로 진행합니다. 컴파일 성공만으로 검증 통과를 판단하지 않고, 테스트벤치의 예상값 비교와 종료 결과를 확인합니다.

Codex에서 XSim을 실행하려면 Vivado 환경을 불러온 같은 터미널에서 `codex`를 실행합니다.

## 📝 날짜별 README 작성 틀

아래 항목을 해당 날짜의 README에 작성합니다.

1. **목표:** 오늘 확인할 동작과 완료 기준
2. **환경:** Ubuntu·Vivado 버전 및 필요한 설정
3. **설계:** 포트, 리셋 방식, 주요 동작
4. **검증 항목:** 정상 동작, 경계 조건, 예외 상황
5. **실행 방법:** 작업 경로와 명령어
6. **결과:** 예상값, 실제값, PASS/FAIL 및 근거
7. **문제 해결:** 증상 → 원인 → 수정 → 재검증
8. **다음 작업:** 남은 검증 항목과 개선할 점

## 🔄 변경 사항 올리기

```bash
cd ~/projects/codex-study
git status
git add README.md 26.09.30/
git diff --cached --stat
git diff --cached
git commit -m "docs: update study notes"
git push
```

다른 날짜를 작업했다면 `git add`의 폴더명을 바꿉니다. 변경 내용을 확인한 뒤 커밋하며, 원격 이력과 충돌하면 강제 push 대신 먼저 이력을 확인합니다.

## ✅ 저장소 관리 원칙

- RTL, 테스트벤치, 제약 파일, 실행 스크립트, 설명 문서를 관리합니다.
- `.gitignore`로 Vivado/XSim 빌드 결과물과 대용량 파형을 제외합니다.
- 개인키, API 토큰, `.env`, 라이선스 파일, 회사 비공개 코드는 올리지 않습니다.
- AI가 작성한 코드도 직접 실행하고 검증합니다.
- 실제로 실행하지 않은 테스트는 PASS로 기록하지 않습니다.

## 🔗 참고 문서

- [Git 공식 문서](https://git-scm.com/doc)
- [GitHub 문서](https://docs.github.com/)
- [Codex CLI 공식 문서](https://developers.openai.com/codex/cli)
- [Vivado Logic Simulation — UG900](https://docs.amd.com/r/en-US/ug900-vivado-logic-simulation)
