#!/bin/bash

# Function to handle errors
handle_error() {
  local error_code=$?  
  local error_line=$1  
  echo "Error in UE $2 for uplink_google on line $error_line with exit code: $error_code"
  exit $error_code
}

# Trap errors and call handle_error with the line number
trap 'handle_error ${LINENO} "$1"' ERR

UEs="ues_uplink_google.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "ue $1 trying to uplink"

if [ "$count" -ge 1 ]; then
  filetxt="$1g.txt"
  ./nr-cli $1 --exec 'ps-list' > "$filetxt"
  str=$(grep "address: " "$filetxt")
  find="address: "
  replace=""
  ip=${str//$find/$replace}
  ip=$(echo $ip | xargs)
  echo "Starting uplink_google by $ip"

  if [ -n "$ip" ]; then
    echo "Uplink from $1 to google"
    ping -c 3 -I $ip 8.8.8.8
    sleep 2
  fi
fi
#rm "$filetxt"
