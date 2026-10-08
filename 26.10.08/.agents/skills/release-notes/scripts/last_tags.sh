#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(git -C "$script_dir" rev-parse --show-toplevel)"

if latest_tag="$(git -C "$repo_root" describe --tags --abbrev=0 2>/dev/null)"; then
  git -C "$repo_root" log --oneline "${latest_tag}..HEAD"
else
  git -C "$repo_root" log --oneline HEAD
fi
