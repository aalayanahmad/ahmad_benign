#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred in uplink_service2_DELAYED exit code: $error_code"
  exit $error_code
}

trap 'handle_error' ERR

UEs="ues_to_use_service2_delayed.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")

if [ "$count" -ge 1 ]; then
  filetxt="$1.txt"
  ./nr-cli $1 --exec 'ps-list' > "$filetxt"
  str=$(grep "address: " "$filetxt")
  find="address: "
  replace=""
  ip=${str//$find/$replace}
  echo "uplink_service2_DELAYED by $1"
  if [ -n "$ip" ]; then
    python3 delayedClient2.py $ip 2
  fi
fi
rm "$filetxt"
