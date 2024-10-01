#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  exit $error_code
}

trap 'handle_error' ERR

UEs="ues_uplink_any.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "ue $1 trying to uplink"

if [ "$count" -ge 1 ]; then
  filetxt="$1.txt"
  ./nr-cli $1 --exec 'ps-list' > "$filetxt"
  str=$(grep "address: " "$filetxt")
  find="address: "
  replace=""
  ip=${str//$find/$replace}
  ip=$(echo $ip | xargs)
  echo "Starting uplink_any by $ip"

  if [ -n "$ip" ]; then
    ping -c 2 -I $ip 8.8.8.8
    sleep 1
  fi
fi
#rm "$filetxt"
