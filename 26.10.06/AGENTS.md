# Repository Guidelines

## Project Structure & Module Organization

This directory, `26.10.06/`, is a dated exercise folder within the parent `codex-study` Git repository. It currently contains `.codex/config.toml` for project-specific Codex settings. There are no source modules, test directories, assets, or dependency manifests yet. Keep new exercise files inside this directory and use descriptive filenames. Introduce separate source, test, or asset directories when an exercise needs them.

## Build, Test, and Development Commands

No build, application startup, or automated test commands are configured. Use these commands from this directory:

- `cat .codex/config.toml`: inspect the project configuration.
- `git status --short -- .`: inspect changes within this exercise folder.
- `git diff -- .`: review tracked changes before committing; inspect untracked files separately.
- `codex -C .`: start Codex for this directory.

Inside the interactive Codex CLI, `/debug-config` displays configuration layers and `/status` displays active permissions. These are CLI input commands, not shell commands.

## Coding Style & Naming Conventions

Keep Markdown concise, with descriptive headings and fenced command examples. Preserve TOML syntax using `snake_case` keys and double-quoted string values. No formatter, linter, or language-specific indentation standard is configured. Follow the conventions of any exercise being extended.

## Testing Guidelines

No testing framework or coverage threshold exists. For configuration changes, start a fresh Codex session and inspect `/debug-config` and `/status`. Document validation steps in the change description. If executable code is added, provide reproducible run and test instructions alongside it.

## Commit & Pull Request Guidelines

Parent repository history uses short, action-oriented subjects such as `Document September 30 Codex prompts and workflow`. Prefer an imperative verb and identify the exercise or behavior changed. Pull requests should explain the purpose, changed files, and validation performed; link relevant issues when available.

## Security & Configuration

The project configuration selects `gpt-6-astra`, `medium` reasoning, and `read-only` sandbox mode. Preserve these defaults unless a task explicitly requires changing them. Keep credentials out of tracked files, and avoid changing user-wide `~/.codex/config.toml` for project-only tasks.
