#!/bin/bash

# Function to handle errors
handle_error() {
  local error_code=$?  
  local error_line=$1  
  echo "Error in UE $2 for uplink on line $error_line with exit code: $error_code"
  exit $error_code
}

# Trap errors and call handle_error with the line number
trap 'handle_error ${LINENO} "$1"' ERR

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
    echo "Uplink from $1 to slice 1"
    ping -c 3 -I $ip 8.8.8.8
    sleep 2
  fi
fi
#rm "$filetxt"
