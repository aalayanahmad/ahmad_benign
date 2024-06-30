#!/bin/bash

handle_error() {
    local error_code=$?
    echo "Error occurred in downlink with exit code: $error_code"
    exit $error_code
}

trap 'handle_error' ERR

trimmed_value=$(echo "$1" | tr -d ' ')
echo "downlink $1"
UEs="ues_performing_downlink.txt"
./nr-cli -d > "$UEs"
if grep -q "$trimmed_value" "$UEs"; then
    echo "downlink value found! performing action..."
fi


ue="ues_downlink.txt"
cp "$UEs" "$ue"

pattern="$1"
count=$(grep -c "$pattern" "$ue")
echo "I am in downlink and there are currently: $count ues"

if [ "$count" -ge 1 ]; then
    filetxt="$1.txt"
    echo "in if"
    ./nr-cli $1 --exec 'ps-list' > "$filetxt"
    str=$(grep "address: " "$filetxt")
    find="address: "
    replace=""
    ip="${str//$find/$replace}"
    echo "downlink for ip: $ip"
    subn="${ip:5:1}"
    if [ -n "$ip" ]; then
        if [ "$subn" = "0" ]; then
            echo "from slice 1"
            ping -I $ip  -c 4 10.60.0.1
        elif [ "$subn" = "1" ]; then
            echo "from slice 2"
            ping -I $ip -c 4 10.61.0.1
        fi
    fi
fi

# Clean up temporary files
# rm -f "$filetxt"
