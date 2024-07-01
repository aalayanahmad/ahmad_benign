#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred in pdu_gnb_release with exit code: $error_code"
  exit $error_code
}

# Set the error handler function to be called on any error
trap 'handle_error' ERR

UEs="pdu_gnb_release.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "I am $1 and I am in pdu_gnb_release and there are currently: $count ues"

if [ "$2" -ge 2 ]; then
    ./nr-cli UERANSIM-gnb-208-93-1 -e "ue-release $2"
fi
