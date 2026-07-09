#!/bin/bash
# Package the oolio-pm plugin as a versioned zip for Cowork local upload.
# Usage: ./scripts/package-plugin.sh [output-dir]   (default: ./dist)
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="${1:-$REPO_ROOT/dist}"

VERSION=$(python3 -c "import json; print(json.load(open('$REPO_ROOT/oolio-pm/.claude-plugin/plugin.json'))['version'])")
MARKET_VERSION=$(python3 -c "import json; print(json.load(open('$REPO_ROOT/.claude-plugin/marketplace.json'))['plugins'][0]['version'])")

if [ "$VERSION" != "$MARKET_VERSION" ]; then
  echo "ERROR: version mismatch — plugin.json says $VERSION, marketplace.json says $MARKET_VERSION. Fix before packaging." >&2
  exit 1
fi

ZIP="$OUT_DIR/oolio-pm-v$VERSION.zip"
mkdir -p "$OUT_DIR"
rm -f "$ZIP"

cd "$REPO_ROOT"
zip -rq "$ZIP" oolio-pm -x "*.DS_Store" -x "*/__pycache__/*"

echo "Packaged v$VERSION -> $ZIP"
unzip -l "$ZIP" | tail -1
