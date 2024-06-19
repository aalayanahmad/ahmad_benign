handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  # Additional error handling code or exit the script
  exit $error_code
}

# Set the error handler function to be called on any error
trap 'handle_error' ERR


UEs="ues_to_release.txt"
sudo $HOME/UERANSIM/build/nr-cli -d > $UEs
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "Count: $count"

if [ "$count" -ge 1 ]; then

sudo $HOME/UERANSIM/build/nr-cli $1 -e "ps-release 1"

fi