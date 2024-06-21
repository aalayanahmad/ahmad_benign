#echo "UPlink"

#trimmed_value=$(echo "$1" | tr -d ' ')
#UEs="fileuesupl.txt"
#sudo $HOME/UERANSIM/build/nr-cli -d > $UEs
#if grep -q $trimmed_value $UEs; then
# echo "uplionk Value found! Performing action..."


handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  # Additional error handling code or exit the script
  exit $error_code
}

# Set the error handler function to be called on any error
trap 'handle_error' ERR


UEs="ues_to_use_service2.txt"
sudo $HOME/UERANSIM/build/nr-cli -d > $UEs
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "count: $count"

if [ "$count" -ge 1 ]; then

#sleep 1
filetxt="$1.txt"
/home/ubuntu/UERANSIM/build/nr-cli $1 --exec "ps-list" > $filetxt
#sudo $HOME/UERANSIM/build/nr-cli $1 --exec "ps-list" > $filetxt
str=$(grep "address: " $filetxt)
find="address: "
replace=""
ip=${str//$find/$replace} 
echo "***service2_uplink***> $ip"
if [ -n "$ip" ]; then
 python3 delayedClient2.py $ip 2
fi


fi
#rm $filetxt


