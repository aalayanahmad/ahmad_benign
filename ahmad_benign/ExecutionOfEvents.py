import math
import time
import subprocess
from multiprocessing import Process

imsi = 'imsi-208930000000' 
ci = 0
cr = 0
cu = 0
cdw = 0
cp = 0
cid = 0
cd = 0  
t = 0#1800,2700
tr=1

myUeslist = []
with open("/home/ubuntu/UERANSIM/script/files/normal_slot5.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        x = line.strip().split(",", 4)
        myUeslist.append(x)

#for i in myUeslist:
# print (i)

def run_command(command):
    subprocess.run(command)#,stdout=subprocess.DEVNULL


while t <= 7230: #2700,3600
    t_plus2 = t + 2
    print("-------------time;", str(t), "---------->+2 seconds:", str(t + 2) + "-------------")
    UEevents = [ue for ue in myUeslist if t <= math.floor(float(ue[2])) < t_plus2]
    processes = []

    for ue in UEevents:
        print(ue)
        if int(ue[1]) == 1:
         try:
            ci += 1
            print("ISSSSSSSSSSSSSSSSSS")
            tr += 1
            filename="ue"+ue[0]+".txt"
            file = open(filename, "w")
            #Write content to the file
            imsivalue=imsi+ue[0]
            print("VALUE OF CR(ISS):"+str(tr))
            file.write(imsivalue+ "," +str(tr)+ "\n")
            #Close the file
            file.close()
       
            p = Process(target=run_command, args=(['bash', './iss.sh', imsi + ue[0], ue[0],str(7777)],))
            processes.append(p)
         except:
            print("error in iss")   
        elif int(ue[1]) == 2:
         try:        
            cr += 1
            print("RegGGGGGGGGGGGGGGGGGGGGG")
            tr += 1
            filename="ue"+ue[0]+".txt"
            file = open(filename, "w")
            #Write content to the file
            imsivalue=imsi+ue[0]
            print("VALUE OF CR(REG):"+str(tr))
            file.write(imsivalue+ "," +str(tr)+ "\n")
            #Close the file
            file.close()
            
            p = Process(target=run_command, args=(['bash', './register.sh', ue[0]],))
            processes.append(p)
         except:
            print("error in registration")   
        elif int(ue[1]) == 3:
         try:
            cu += 1
            p = Process(target=run_command, args=(['bash', './uplink.sh', imsi + ue[0]],))
            processes.append(p)
         except:
            print("error in uplink")   
        elif int(ue[1]) == 4:
         try:        
            cdw += 1
            p = Process(target=run_command, args=(['bash', './downlink.sh', imsi + ue[0]],))
            processes.append(p)
         except:
            print("error in donwlink")   
        elif int(ue[1]) == 5:
         try:        
            cp += 1
            p = Process(target=run_command, args=(['bash', './ueRelease.sh', imsi + ue[0]],))
            processes.append(p)
         except:
            print("error in PDU session release")   
        elif int(ue[1]) == 6:
         try:        
            cid += 1
            # imsi + ue[0],it was deleted becaseu gnb was modified.
            p = Process(target=run_command, args=(['bash', './gnbBRelease.sh', imsi + ue[0], ue[0]],))
            processes.append(p)
         except:
            print("error in GNB release")   
        else:
         try:          
            cd += 1
            p = Process(target=run_command, args=(['bash', './Deregister.sh', imsi + ue[0]],))
            processes.append(p)
         except:
            print("error in deregistration")     

    for p in processes:
       p.start()

    #for p in processes:
     #   p.join()

    time.sleep(2)
    t += 2

print("ci:" + str(ci) + "   cr:" + str(cr) + "   cu:" + str(cu) + "   cdw:" + str(cdw) + "   cp:" + str(cp) + "   cid:" + str(cid) + "   cd:" + str(cd))
"""
import library as lb
list_events=lb.non_compromised_ues_events(0)
"""