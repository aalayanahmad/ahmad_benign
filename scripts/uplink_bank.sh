#!/bin/bash

# Function to handle errors
handle_error() {
  local error_code=$?  
  local error_line=$1  
  echo "Error in UE $2 for uplink_bank on line $error_line with exit code: $error_code"
  exit $error_code
}

# Trap errors and call handle_error with the line number
trap 'handle_error ${LINENO} "$1"' ERR


UEs="ues_to_use_banking.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")

if [ "$count" -ge 1 ]; then
  filetxt="$1b.txt"
  ./nr-cli $1 --exec 'ps-list' > "$filetxt"
  str=$(grep "address: " "$filetxt")
  find="address: "
  replace=""
  ip=${str//$find/$replace}
  ip=$(echo $ip | xargs)
  echo "uplink_bank by $1"
  if [ -n "$ip" ]; then
    java BankClient $ip
  fi
fi
#rm "$filetxt"