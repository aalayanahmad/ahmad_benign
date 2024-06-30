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
echo "I am in pdu_ugnb_release and there are currently: $count ues"

if [ "$count" -ge 1 ]; then
  echo "second parameter $2"
  oldtxt=$(sed -n '1p' "/ueransim/ue$2.txt")
  ueid="${oldtxt:21}"
  #ueid=$(echo "$oldtxt" | cut -d',' -f2)
  
  echo "ueid: $ueid"

  if [ -n "$ueid" ]; then
    ./nr-cli UERANSIM-gnb-208-93-1 -e "ue-release $ueid"
  fi
fi
