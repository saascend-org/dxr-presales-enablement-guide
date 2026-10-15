#!/bin/bash
# Rebuild the password-gated Pre-Sales guide and push it to GitHub Pages.
# Prompts for the password so it never lands in a file, the repo or shell history.
set -euo pipefail
cd "$(dirname "$0")"
read -rsp "Guide password: " PW; echo
[ -n "$PW" ] || { echo "No password entered - nothing published."; exit 1; }
python3 build.py
printf %s "$PW" | node build/encrypt.js -
unset PW
rm -f build/index.plain.html
git add index.html assets/img/dxr-cyber-logo.png .gitignore README.md publish.sh build.py build/encrypt.js
git commit -m "Publish Pre-Sales enablement guide $(date +%Y-%m-%d)" || echo "(no changes to commit)"
git push origin main
echo "Live in about a minute: https://saascend-org.github.io/dxr-presales-enablement-guide/"
