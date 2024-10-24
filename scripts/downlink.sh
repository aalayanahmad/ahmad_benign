#!/bin/bash

# Function to handle errors
handle_error() {
  local error_code=$?  
  local error_line=$1  
  echo "Error in UE $2 for downlink on line $error_line with exit code: $error_code"
  exit $error_code
}

# Trap errors and call handle_error with the line number
trap 'handle_error ${LINENO} "$1"' ERR

ue="ues_downlink.txt"
./nr-cli -d > "$ue"
echo "ue $1 trying to downlink"
pattern="$1"
count=$(grep -c "$pattern" "$ue")

if [ "$count" -ge 1 ]; then
    filetxt="$1.txt"
    ./nr-cli "$1" --exec 'ps-list' > "$filetxt"
    str=$(grep "address: " "$filetxt")
    find="address: "
    replace=""
    ip="${str//$find/$replace}"
    echo "Downlink for IP: $ip"
    subn="${ip:5:1}"
    if [ -n "$ip" ]; then
    echo "subn: $subn"
        if [ "$subn" = "0" ]; then
            echo "Downlink from $1 to slice 1"
            ip=$(echo $ip | xargs)
            ping -c 3 -I "$ip" 10.60.0.1
            sleep 1
        elif [ "$subn" = "1" ]; then
            echo "Downlink from $1 to slice 2"
            ip=$(echo $ip | xargs)
            ping -c 1 -I "$ip" 10.61.0.1
            sleep 1
        fi
    fi
fi

#rm -f "$filetxt"
