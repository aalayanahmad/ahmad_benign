sudo $HOME/UERANSIM/build/nr-ue -c $HOME/UERANSIM/config/ue$1.yaml -n 1  & sleep 2
#textfile="ueidlist.txt"
#$HOME/UERANSIM/build/nr-cli UERANSIM-gnb-208-93-1 -e ue-list > $textfile
#val=$(head -n 1 $textfile)
#echo $val
#find="- ue-id: "
#replace=""
#ueid=${val//$find/$replace}
#echo $ueid
##echo "imsi-208930000000$1,$ueid" >> ueId.txt
#echo "imsi-208930000000$1,$ueid" >> ue$1.txt
 