# #!/bin/bash

# handle_error() {
#   local error_code=$?
#   echo "Error occurred in uplink_service2_delayed with exit code: $error_code"
#   # Additional error handling code or exit the script
#   exit $error_code
# }

# # Set the error handler function to be called on any error
# trap 'handle_error' ERR

# UEs="ues_to_use_service1.txt"
# ./nr-cli -d > "$UEs"
# pattern="$1"
# count=$(grep -c "$pattern" "$UEs")
# #!/bin/bash

# handle_error() {
#   local error_code=$?
#   echo "Error occurred with exit code: $error_code"
#   # Additional error handling code or exit the script
#   exit $error_code
# }

# # Set the error handler function to be called on any error
# trap 'handle_error' ERR

# UEs="ues_to_use_service2_delayed.txt"
# ./nr-cli -d > "$UEs"
# pattern="$1"
# count=$(grep -c "$pattern" "$UEs")
# echo "I am in uplink_service2_delayed and there are currently: $count ues"

# if [ "$count" -ge 1 ]; then
#   filetxt="$1.txt"
#   ./nr-cli $1 --exec 'ps-list' > "$filetxt"
#   str=$(grep "address: " "$filetxt")
#   find="address: "
#   replace=""
#   ip=${str//$find/$replace}
#   echo "delayed_service2_uplink $ip"
#   if [ -n "$ip" ]; then
#     python3 attackClient2.py $ip 2
#   fi
# fi
# #rm "$filetxt"
