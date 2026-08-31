#!/bin/bash
CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
PORT=$1; VARIANT=$2; RUNS=$3
for i in $(seq 1 $RUNS); do
  D=$(mktemp -d)
  $CHROME --headless --no-sandbox --disable-gpu --disable-dev-shm-usage \
    --user-data-dir=$D --disable-features=NetworkServiceInProcess \
    --window-size=1280,900 --virtual-time-budget=60000 \
    --dump-dom "http://127.0.0.1:$PORT/$VARIANT" 2>/dev/null \
    | grep -oE '<pre id="__M__">[^<]*</pre>' | sed 's/<[^>]*>//g'
  rm -rf $D
done
