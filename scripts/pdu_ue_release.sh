#!/bin/bash

# Function to handle errors
handle_error() {
  local error_code=$?  
  local error_line=$1  
  echo "Error in UE $2 for ue_release on line $error_line with exit code: $error_code"
  exit $error_code
}

# Trap errors and call handle_error with the line number
trap 'handle_error ${LINENO} "$1"' ERR

UEs="pdu_ue_release.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "UE $1 wants to perform pdu_ue_release and count is $count"

if [ "$count" -ge 1 ]; then
  ./nr-cli "$1" -e 'ps-release 1'
fi
