#!/bin/bash

handle_error() {
  local error_code=$?
  local line_number=$1
  local command=$2
  echo "Error occurred in pdu_ue_release for $1 when executing $command at line $line_number with exit code: $error_code"
  exit $error_code
}

trap 'handle_error ${LINENO} "$BASH_COMMAND"' ERR

UEs="pdu_ue_release.txt"
sudo build/nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")

if [ "$count" -ge 1 ]; then
  sudo build/nr-cli "$1" -e 'ps-release 1' & sleep 2
fi
