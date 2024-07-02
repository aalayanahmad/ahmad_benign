#!/bin/bash

handle_error() {
    local error_code=$?
    echo "Error occurred in downlink with exit code: $error_code"
    exit $error_code
}

trap 'handle_error' ERR

ue="ues_downlink.txt"
./nr-cli -d > "$ue"

pattern="$1"
count=$(grep -c "$pattern" "$ue")

if [ "$count" -ge 1 ]; then
    filetxt="$1.txt"
    ./nr-cli $1 --exec 'ps-list' > "$filetxt"
    str=$(grep "address: " "$filetxt")
    find="address: "
    replace=""
    ip="${str//$find/$replace}"
    echo "downlink for ip: $ip"
    subn="${ip:5:1}"
    if [ -n "$ip" ]; then
        if [ "$subn" = "0" ]; then
            echo "downlink from $1 to slice 1"
            ping -c 3 -I $ip 10.60.0.1
        elif [ "$subn" = "1" ]; then
            echo "downlink from $1 to slice 2"
            ping -c 3 -I $ip 10.61.0.1
        fi
    fi
fi

rm -f "$filetxt"
