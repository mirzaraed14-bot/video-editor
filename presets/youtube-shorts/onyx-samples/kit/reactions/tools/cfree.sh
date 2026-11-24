#!/usr/bin/env bash
# cfree.sh [MB]: wait (poll 60 s) until C: has >= MB (default 1500) free. MB=1500 is the render-queue guard (renders write to X:, so only 300 MB of C: temp is needed); 1501+ = a Premiere write (1.5 GB).
N=${1:-1500}; [ "$N" = 1500 ] && N=300
while true; do F=$(df -m /c | awk 'END{print $4}'); [ "$F" -ge "$N" ] && break; echo "C: ${F} MB free < $N, waiting"; sleep 60; done
