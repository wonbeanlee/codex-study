# codex-study
codex-study
Ubuntu에서 Codex와 함께 배우는 RTL 설계 · SystemVerilog 검증 · 개발 자동화

실습 코드를 직접 실행하고 결과를 확인하며, 날짜별로 문제 해결 과정을 기록하는 개인 학습 저장소입니다.
🎯 학습 목표
- Linux 터미널과 Git으로 개발 환경 관리하기
- Codex를 활용해 코드 분석, 테스트벤치 작성, 오류 수정하기
- Vivado/XSim으로 Verilog·SystemVerilog 동작 검증하기
- 실행 명령과 예상 결과를 남겨 다시 재현할 수 있는 실습 만들기
🛠️ 개발 환경
구분	구성
가상화	VMware
운영체제	Ubuntu 24.04 계열, x86_64
편집기	VS Code
AI 개발 도구	Codex CLI
RTL 설계·시뮬레이션	AMD Vivado 2026.1 / XSim
버전 관리	Git / GitHub

실제 도구 실행 여부와 버전은 각 날짜의 실습 기록에 남깁니다. 이 표는 모든 기능의 검증 완료를 의미하지 않습니다.
📚 학습 기록
날짜	주제	기록
2026-09-30	Ubuntu 개발 환경 및 GitHub 연결	[26.09.30 폴더](./26.09.30/)


새 실습은 26.10.01/README.md처럼 날짜별 폴더에 추가합니다. 루트 README는 전체 안내, 날짜별 README는 실습 상세 기록으로 사용합니다.
📁 권장 폴더 구성
다음은 확장할 때 사용할 예시입니다. README만 추가한다고 아래 파일들이 자동으로 생성되지는 않습니다.

🚀 Ubuntu에서 시작하기
이미 저장소가 있는 경우, 로컬 변경을 먼저 확인하고 최신 내용을 가져옵니다.
cd ~/projects/codex-study
git status
git pull --ff-only
code README.md
로컬 수정이 있으면 커밋하거나 보관한 뒤 pull합니다. VS Code에서 Ctrl + Shift + V를 누르면 Markdown 미리보기를 볼 수 있습니다.
처음 받는 PC에서는 GitHub SSH 인증을 설정한 뒤 실행합니다.
mkdir -p ~/projects
cd ~/projects
git clone git@github.com:wonbeanlee/codex-study.git
cd codex-study
code .
🤖 Codex 활용 예시
프로젝트 폴더에서 실행합니다.
cd ~/projects/codex-study
codex
