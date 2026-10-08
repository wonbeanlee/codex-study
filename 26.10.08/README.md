# 2026-10-08 Codex 작업 기록

이 문서는 오늘 Codex와 나눈 요청과 `26.10.08` 폴더의 최종 구성을 기록합니다. GitHub MCP Server 파일을 보관하고, 릴리스 노트 작성 스킬에 마지막 태그 이후 커밋을 확인하는 스크립트를 추가했습니다.

## 1. 대화에서 요청한 작업

### 릴리스 노트 작성

최근 변경을 바탕으로 한국어 릴리스 노트를 작성했습니다. 저장소에 태그가 없어 당시 존재하는 커밋을 기준으로 정리했습니다.

### 마지막 태그 이후 커밋을 출력하는 스크립트

`.agents/skills/release-notes/scripts/last_tags.sh`를 만들고 릴리스 노트 스킬의 1단계에서 사용하도록 요청했습니다. 스크립트는 마지막 태그 이후 커밋을 한 줄씩 출력하며, 태그가 없으면 전체 커밋 목록을 출력합니다.

### 저장소에 올리고 폴더별로 정리

저장소 주소를 `https://github.com/wonbeanlee/codex-study`로 지정해 로컬 변경을 정리해 올리도록 요청했습니다. 이어서 `26.10.08` 폴더에 `.codex`와 README를 넣도록 방향을 정리했고, 마지막으로 `.agents`도 포함하고 README에 대화 내용을 기록하도록 요청했습니다.

## 2. 파일 구성

```text
26.10.08/
├── .agents/
│   └── skills/
│       └── release-notes/
│           ├── SKILL.md
│           └── scripts/
│               └── last_tags.sh
├── .codex/
│   └── bin/
│       ├── LICENSE
│       ├── README.md
│       └── github-mcp-server
└── README.md
```

## 3. 릴리스 노트 스킬

`SKILL.md`는 최근 태그 이후의 변경을 새 기능, 버그 수정, 개선, 문서로 분류하고 사용자 관점의 간결한 한국어 릴리스 노트를 작성하도록 안내합니다. 첫 단계에서 `last_tags.sh`를 실행해 커밋 목록을 확인합니다.

스크립트는 실행 위치와 관계없이 저장소 루트를 찾아 `git log --oneline`을 실행합니다. 저장소에 태그가 없으면 `HEAD`까지의 전체 커밋을 보여줍니다.

## 4. Codex와 GitHub MCP Server 파일

`.codex/bin/`에는 GitHub MCP Server 실행 파일, 라이선스, upstream 사용 안내가 있습니다. MCP 호스트 및 GitHub 인증 설정은 `.codex/bin/README.md`를 참고합니다. 인증 정보는 이 폴더에 포함하지 않습니다.

## 5. 저장소

[GitHub에서 26.10.08 폴더 보기](https://github.com/wonbeanlee/codex-study/tree/main/26.10.08)
