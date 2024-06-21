##filetxt="$HOME/UERANSIM/script/ueID.txt"
#filetxt="$HOME/UERANSIM/script/ue$2.txt"
#tt=$1
#str=$(grep $tt $filetxt | tail -1)
#ueid="${str:21}"

#Ihave to change ue$1 for ue$2 if I uncomment the previous code and add the imsi in the normal.py
handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  # Additional error handling code or exit the script
  exit $error_code
}

# Set the error handler function to be called on any error
trap 'handle_error' ERR


UEs="fileuesGnbrelease.txt"
sudo $HOME/UERANSIM/build/nr-cli -d > $UEs
pattern="$1"
count=$(grep -c "$pattern" "$UEs")
echo "Count: $count"

if [ "$count" -ge 1 ]; then


echo "second parameter $2"
oldtxt=$(sed -n '1p' $HOME/UERANSIM/script/test/ue$2.txt)
ueid="${oldtxt:21}"
echo "-------------ueid-------------"$ueid

if [ -n "$ueid" ]; then
 sudo $HOME/UERANSIM/build/nr-cli UERANSIM-gnb-208-93-1 -e "ue-release $ueid" 
fi

fi