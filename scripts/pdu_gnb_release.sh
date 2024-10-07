#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error for UE $1 during gnb_release with exit code: $error_code"
  exit $error_code
}

trap 'handle_error "1"' ERR

UEs="pdu_gnb_release.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "UE $1 wants to perform pdu_gnb_release and count is $count"

if [ "$count" -ge 1 ]; then
  # Read ue$1.txt to get the ueid
  ue_file="/ueransim/ue$2.txt"

  # Check if the file exists
  if [ -f "$ue_file" ]; then
      # Read the ueid directly from the file
      ueid=$(cat "$ue_file")
      echo "-------------ue$1 has an id------------- $ueid"
      # Ensure ueid is not empty before calling the command
      if [ -n "$ueid" ]; then
          ./nr-cli UERANSIM-gnb-208-93-1 -e "ue-release $ueid"
      else
          echo "ueid is empty. Cannot perform ue-release."
      fi
  else
      echo "File $ue_file does not exist."
  fi
fi


