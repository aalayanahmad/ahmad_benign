#echo "Downlink"

#trimmed_value=$(echo "$1" | tr -d ' ')
#UEs="fileuesdown.txt"
#sudo $HOME/UERANSIM/build/nr-cli -d > $UEs
#if grep -q $trimmed_value $UEs; then
# echo "Donwlionk Value found! Performing action..."


handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  # Additional error handling code or exit the script
  exit $error_code
}

# Set the error handler function to be called on any error
trap 'handle_error' ERR


ues="ues_downlink.txt"

sudo $HOME/UERANSIM/build/nr-cli -d > $UEs
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "Count: $count"

if [ "$count" -ge 1 ]; then

#sleep 1
filetxt="$1.txt"
sudo $HOME/UERANSIM/build/nr-cli $1 --exec "ps-list" > $filetxt
str=$(grep "address: " $filetxt)
find="address: "
replace=""
ip=${str//$find/$replace} 
echo "ip address:::::::----->"$ip
subn=${ip:5:1}
echo "***subnnnnnnnnnnnnnnnnnn*** downlink:$subn"

if [ -n "$ip" ]; then
if [ "$subn" = "0" ]
then
 echo "0000000000"
 ping -c 1 -I 10.60.0.1 $ip 
elif [ "$subn" = "1" ]
then
 echo "1111111111111111111111"
 ping -c 1 -I 10.61.0.1 $ip 
elif [ "$subn" = "2" ]
then
 echo "222222222222222"
 ping -c 1 -I 10.62.0.1 $ip 
elif [ "$subn" = "3" ]
then
 echo "3333333333333"
 ping -c 1 -I 10.63.0.1 $ip
fi 
fi


fi
#rm $filetxt
