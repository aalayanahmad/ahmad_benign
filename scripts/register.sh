#!/bin/bash

UE_GNB_ID_COUNTER_FILE="ue_gnb_id_counter.txt" # Store the ue_gnb_id global variable
SEMAPHORE_FILE="/tmp/ue_gnb_id_semaphore.lock"  # Semaphore file

# Initialize the counter file if it doesn't exist
if [ ! -f "$UE_GNB_ID_COUNTER_FILE" ]; then
    echo 2 > "$UE_GNB_ID_COUNTER_FILE"  # Start at 2
fi


handle_error() {
    local error_code=$?
    echo "Error for UE $1 while trying registeration with exit code: $error_code"
    exit $error_code
}

# Trap errors
trap 'handle_error "$1"' ERR

echo "UE $1 is trying to register..."

# Use flock to ensure exclusive access to the counter file
{
    # This will block until it can acquire the lock
    flock 200

    # Read the current value
    counter=$(cat "$UE_GNB_ID_COUNTER_FILE")

    # Save the new value back to the file
    counter=$((counter + 1))
    # Replace this with your actual command

    echo "$counter" > "$UE_GNB_ID_COUNTER_FILE" #update counter value in the global coutner file
    echo "$counter" > "ue$1.txt" #save the id of the current ue

} 200>"$SEMAPHORE_FILE"  
./nr-ue -c config/ue"$1".yaml -n 1
#sleep 2
