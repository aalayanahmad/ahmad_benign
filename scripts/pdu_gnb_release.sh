#!/bin/bash

handle_error() {
  local error_code=$?
  local line_number=$1
  local command=$2
  echo "Error occurred in pdu_gnb_release at $1 when executing $command at line $line_number with exit code: $error_code"
  exit $error_code
}

trap 'handle_error ${LINENO} "$BASH_COMMAND"' ERR

UEs="pdu_gnb_release.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "I am $1 and I am in pdu_gnb_release"

if [ "$count" -ge 1 ]; then
  if [ "$2" -ge 3 ]; then
      ./nr-cli UERANSIM-gnb-208-93-1 -e "ue-release $2" & sleep 2
  fi
fi
