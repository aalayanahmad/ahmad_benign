#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  exit $error_code
}

trap 'handle_error' ERR

UEs="pdu_gnb_release.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "I am $1 and I am in pdu_gnb_release"

if [ "$count" -ge 1 ]; then
  if [ "$2" -ge 3 ]; then
      sleep 1
      ./nr-cli UERANSIM-gnb-208-93-1 -e "ue-release $2"
  fi
fi

# UEs="pdu_gnb_release.txt"
# ./nr-cli -d > "$UEs"
# pattern="$1"
# count=$(grep -c "$pattern" "$UEs")
# echo "UE $1 wants to perform pdu_gnb_release and count is $count"


# if [ "$count" -ge 1 ]; then
#   echo "UE $1 id is $2"
#   createdtxt=$(sed -n '1p' /ueransim/ue$2.txt)
#   ueid="${createdtxt:21}"
#   echo "-------------ueid-------------"$ueid
# if [ -n "$ueid" ]; then
#  ./nr-cli UERANSIM-gnb-208-93-1 -e "ue-release $ueid" 
# fi

# fi
