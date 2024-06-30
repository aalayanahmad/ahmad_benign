 #!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred in uplink_any with exit code: $error_code"
  # Additional error handling code or exit the script
  exit $error_code
}

# Set the error handler function to be called on any error
trap 'handle_error' ERR

UEs="ues_uplink_any.txt"
./nr-cli -d > "$UEs"
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "I am in uplink_any and there are currently: $count UEs"

if [ "$count" -ge 1 ]; then
  filetxt="$1.txt"
  ./nr-cli $1 --exec 'ps-list' > "$filetxt"
  str=$(grep "address: " "$filetxt")
  find="address: "
  replace=""
  ip=${str//$find/$replace}
  ip=$(echo $ip | xargs)  # Trim leading and trailing whitespace
  echo "uplink_any $ip"

  if [ -n "$ip" ]; then
    ping -I $ip -c 4 8.8.8.8
  fi
fi
#rm "$filetxt"
