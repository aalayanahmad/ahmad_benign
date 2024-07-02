#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred in uplink_service1_delayed with exit code: $error_code"
  # Additional error handling code or exit the script
  exit $error_code
}

# Set the error handler function to be called on any error
trap 'handle_error' ERR

UEs="ues_to_use_service1_delayed.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "I am in uplink_service1_delayed and there are currently: $count ues"

if [ "$count" -ge 1 ]; then
  filetxt="$1.txt"
  ./nr-cli $1 --exec 'ps-list' > "$filetxt"
  str=$(grep "address: " "$filetxt")
  find="address: "
  replace=""
  ip=${str//$find/$replace}
  echo "delayed_service1_uplink $ip"
  if [ -n "$ip" ]; then
    java client1 $ip 2
  fi
fi
#rm "$filetxt"
