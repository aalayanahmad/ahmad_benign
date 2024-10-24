#!/bin/bash

# Function to handle errors
handle_error() {
  local error_code=$?
  local error_line=$1
  echo "Error while --CHECKING IF REGISTERED-- on line $error_line with exit code: $error_code"
  exit $error_code
}

# Trap errors and call handle_error with the line number
trap 'handle_error ${LINENO}' ERR

attack_ues_yamls=(ue105.yaml ue111.yaml ue128.yaml ue130.yaml ue133.yaml ue138.yaml ue140.yaml ue143.yaml ue148.yaml ue151.yaml ue153.yaml)
attack_ues_imsi=(imsi-208930000000105 imsi-208930000000111 imsi-208930000000128 imsi-208930000000130 imsi-208930000000133 imsi-208930000000138 imsi-208930000000140 imsi-208930000000143 imsi-208930000000148 imsi-208930000000151 imsi-208930000000153)

UEs="yaml_for_ues_to_use_for_attack.txt"
how_many_registered="how_many_registered.txt"

# Clear or create the how_many_registered file
> "$how_many_registered"

# Capture current registered UEs
./nr-cli -d > "$UEs" || { echo "Failed to retrieve UEs"; exit 1; }

# Initialize counter for registered UEs
registered_count=0

for index in "${!attack_ues_yamls[@]}"; do
    item="${attack_ues_yamls[$index]}"
    pattern="${attack_ues_imsi[$index]}"
    
    # Search for IMSI in the current list of UEs
    count=$(grep -cw "$pattern" "$UEs")
    
    if [ "$count" -ge 1 ]; then #the ue already registered
        echo "$item is registered"
        ((registered_count++))  # Increment the counter
    else #register the ue
        ./nr-ue -c config/$item || { echo "Failed to register $item"; exit 1; }
    fi
done

# Compare the counter to the length of the array
if [ "$registered_count" -eq "${#attack_ues_yamls[@]}" ]; then
    echo "true" > "$how_many_registered"
else
    echo "false" > "$how_many_registered"
fi
