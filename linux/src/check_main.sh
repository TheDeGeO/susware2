#!/bin/bash
function ignore_ctrlc {echo "ignored"}

trap ignore_ctrlc SIGINT SIGTERM
while true; do

  pgrep -x python  && echo "Process found" || echo "Process not found" && python3 main__copy.py
  sleep 3
  $SHELL
done