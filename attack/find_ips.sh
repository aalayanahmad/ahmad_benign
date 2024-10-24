#!/bin/bash

# Function to handle errors
handle_error() {
  local error_code=$?
  local error_line=$1
  echo "Error while --FINDING IPs-- on line $error_line with exit code: $error_code"
  exit $error_code
}

# Trap errors and call handle_error with the line number
trap 'handle_error ${LINENO}' ERR

attack_ues=(imsi-208930000000105 imsi-208930000000111 imsi-208930000000128 imsi-208930000000130 imsi-208930000000133 imsi-208930000000138 imsi-208930000000140 imsi-208930000000143 imsi-208930000000148 imsi-208930000000151 imsi-208930000000153)

UEs="ues_to_use_for_attack.txt"
./nr-cli -d > "$UEs"  #get the current list of ues

# Loop through each UE and check registration status
for item in "${attack_ues[@]}"; do
    pattern="$item"
    
    # Check if the IMSI is present
    count=$(grep -c "$pattern" "$UEs")
    
    if [ "$count" -ge 1 ]; then
        echo "$item is registered"
        filetxt="${item}_attack.txt"
        iptxt="${item}_attack_ip.txt"

        # Fetch the UE process list and save it to file
        ./nr-cli "$item" --exec 'ps-list' > "$filetxt"

        # Extract the IP address from the file
        str=$(grep "address: " "$filetxt")
        
        # Check if the address was found
        if [[ -n "$str" ]]; then
            # Replace "address: " and trim whitespace
            find="address: "
            replace=""
            ip=${str//$find/$replace}
            ip=$(echo "$ip" | xargs)  # Trim extra whitespace

            echo "$ip" > "$iptxt"  # Save IP to file
        else
            echo "No address found for $item in $filetxt"
        fi
    fi
done
