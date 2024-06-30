#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred in pdu_ue_release with exit code: $error_code"
  # Additional error handling code or exit the script
  exit $error_code
}

# Set the error handler function to be called on any error
trap 'handle_error' ERR

UEs="pdu_ue_release.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "I am in pdu_ue_release and there are currently: $count ues"

if [ "$count" -ge 1 ]; then
  ./nr-cli $1 -e 'ps-release 1'
fi
