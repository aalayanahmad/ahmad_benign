#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  exit $error_code
}

trap 'handle_error' ERR

echo "UE $1 is trying to register..."

./nr-ue -c config/ue$1.yaml -n 1  
sleep 2

# #!/bin/bash

# UE_GNB_ID_COUNTER_FILE="ue_gnb_id_counter.txt" # Store the ue_gnb_id global variable
# SEMAPHORE_FILE="/tmp/ue_gnb_id_semaphore.lock"  # Semaphore file

# # Initialize the counter file if it doesn't exist
# if [ ! -f "$UE_GNB_ID_COUNTER_FILE" ]; then
#     echo 2 > "$UE_GNB_ID_COUNTER_FILE"  # Start at 2
# fi

# # Function to handle errors
# handle_error() {
#     local error_code=$?
#     echo "Error occurred with exit code: $error_code"
#     exit $error_code
# }

# # Trap errors
# trap 'handle_error' ERR

# echo "UE $1 is trying to register..."

# # Use flock to ensure exclusive access to the counter file
# {
#     # This will block until it can acquire the lock
#     flock 200

#     # Read the current value
#     counter=$(cat "$UE_GNB_ID_COUNTER_FILE")

#     # Replace this with your actual command
#     ./nr-ue -c config/ue"$1".yaml -n 1

#     # Increment the counter and assign a unique ID to this UE
#     ueid=$counter

#     # Save the new value back to the file
#     counter=$((counter + 1))
#     echo "$counter" > "$UE_GNB_ID_COUNTER_FILE"

# } 200>"$SEMAPHORE_FILE"  # Use file descriptor 200 for the lock

# # Write the unique identifier to the corresponding UE file
# echo "$ueid" > "ue$1.txt"

# sleep 2
