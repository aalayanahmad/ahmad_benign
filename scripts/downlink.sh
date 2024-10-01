#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  exit $error_code
}

trap 'handle_error' ERR

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
            ping -c 2 -I "$ip" 10.61.0.1
            sleep 1
        fi
    fi
fi

#rm -f "$filetxt"
