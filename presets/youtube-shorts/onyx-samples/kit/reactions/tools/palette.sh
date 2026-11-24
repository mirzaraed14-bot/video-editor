#!/usr/bin/env bash
# palette.sh <job>: copy the SFX palette (assets/sfx/onyx-reactions: batch-9 clean Epidemic originals in src/, the prepped v3x-* slices, slices.json) into projects/<job>/sfx/.
# assets/sfx/ is gitignored (audio never goes in the kit tree). No new searches or downloads: sfxassign3 picks from these.
cd "$(dirname "${BASH_SOURCE[0]}")/../../../../../.." || exit 1
if [ $# -lt 1 ] || [ "$1" = "--help" ]; then sed -n 2,3p "$0"; exit 0; fi
J=projects/$1; mkdir -p $J/sfx/src
cp -n assets/sfx/onyx-reactions/*.wav assets/sfx/onyx-reactions/slices.json $J/sfx/
cp -n assets/sfx/onyx-reactions/src/*.wav $J/sfx/src/
echo "palette: $(ls $J/sfx/v3x-*.wav | wc -l) slices, $(ls $J/sfx/src | wc -l) originals in $J/sfx"
