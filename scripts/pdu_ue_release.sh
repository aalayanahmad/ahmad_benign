#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  exit $error_code
}

trap 'handle_error' ERR

UEs="pdu_ue_release.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "UE $1 wants to perform pdu_ue_release and count is $count"

if [ "$count" -ge 1 ]; then
  ./nr-cli "$1" -e 'ps-release 1'
  sleep 1
fi
