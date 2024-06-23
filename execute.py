import math
import time
import subprocess
from multiprocessing import Process

imsi = 'imsi-208930000000' 
cr = 0
cua = 0
cus1 = 0
cus2 = 0
cus1d = 0
cus2d = 0
cd = 0
cpu = 0
cpg = 0
ci = 0
cd = 0  

t = 0 #1800,2700
tr = 1
 
ue_list = []
with open("/home/ubuntu/UERANSIM/script/files/normal_slot1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        x = line.strip().split(",", 4)
        ue_list.append(x)


def run_command(command):
    subprocess.run(command)


while t <= 7230: #2700,3600
    t_plus2 = t + 2
    print("-------------time;", str(t), "---------->+2 seconds:", str(t + 2) + "-------------")
    ue_events = [ue for ue in ue_list if t <= math.floor(float(ue[2])) < t_plus2]
    processes = []

    for ue in ue_events:
        match ue[1]:
         case 1:
            try:
               cr += 1
               print("registration")
               tr += 1
               file_name = "ue" + ue[0] + ".txt"
               file = open(file_name, "w")
               
               imsi_value = imsi+ue[0]
               file.write(imsi_value + "," +str(tr) + "\n")
               file.close()
               p = Process(target=run_command, args=(['bash', './register.sh', imsi + ue[0],],))
               processes.append(p)
               continue
            except:
               print("error in registration")   
         case 2:
            try:        
               cua += 1
               print("uplink_any")
               tr += 1
               file_name = "ue" + ue[0] + ".txt"
               file = open(file_name, "w")
               imsi_value = imsi + ue[0]
               file.write(imsi_value+ "," + str(tr) + "\n")
               file.close()
               p = Process(target=run_command, args=(['bash', './uplink_any.sh', ue[0]],))
               processes.append(p)
               continue
            except:
               print("error in uplink_any")   
         case 3:
            try:        
               cus1 += 1
               print("uplink_service1")
               tr += 1
               file_name = "ue" + ue[0] + ".txt"
               file = open(file_name, "w")
               imsi_value = imsi + ue[0]
               file.write(imsi_value+ "," + str(tr) + "\n")
               file.close()
               p = Process(target=run_command, args=(['bash', './uplink_service1.sh', ue[0]],))
               processes.append(p)
               continue
            except:
               print("error in uplink_service1")   
         case 4:
            try:        
               cus2 += 1
               print("uplink_service2")
               tr += 1
               file_name = "ue" + ue[0] + ".txt"
               file = open(file_name, "w")
               imsi_value = imsi + ue[0]
               file.write(imsi_value+ "," + str(tr) + "\n")
               file.close()
               p = Process(target=run_command, args=(['bash', './uplink_service2.sh', ue[0]],))
               processes.append(p)
               continue
            except:
               print("error in uplink_service2") 
         case 5:
            try:        
               cus1d += 1
               print("uplink_service1_delayed")
               tr += 1
               file_name = "ue" + ue[0] + ".txt"
               file = open(file_name, "w")
               imsi_value = imsi + ue[0]
               file.write(imsi_value+ "," + str(tr) + "\n")
               file.close()
               p = Process(target=run_command, args=(['bash', './uplink_service1_delayed.sh', ue[0]],))
               processes.append(p)
               continue
            except:
               print("error in uplink_service1_delayed") 
         case 6:
            try:        
               cus2d += 1
               print("uplink_service2_delayed")
               tr += 1
               file_name = "ue" + ue[0] + ".txt"
               file = open(file_name, "w")
               imsi_value = imsi + ue[0]
               file.write(imsi_value+ "," + str(tr) + "\n")
               file.close()
               p = Process(target=run_command, args=(['bash', './uplink_service2_delayed.sh', ue[0]],))
               processes.append(p)
               continue
            except:
               print("error in uplink_service2_delayed")  
         case 7:
            try:        
               cd += 1
               print("downlink")
               tr += 1
               file_name = "ue" + ue[0] + ".txt"
               file = open(file_name, "w")
               imsi_value = imsi + ue[0]
               file.write(imsi_value+ "," + str(tr) + "\n")
               file.close()
               p = Process(target=run_command, args=(['bash', './downlink.sh', ue[0]],))
               processes.append(p)
               continue
            except:
               print("error in downlink")     
         case 8:
            try:        
               cd += 1
               print("pdu_ue_release")
               tr += 1
               file_name = "ue" + ue[0] + ".txt"
               file = open(file_name, "w")
               imsi_value = imsi + ue[0]
               file.write(imsi_value+ "," + str(tr) + "\n")
               file.close()
               p = Process(target=run_command, args=(['bash', './pdu_ue_release.sh', ue[0]],))
               processes.append(p)
               continue
            except:
               print("error in pdu_ue_release")    
         case 9:
            try:        
               cd += 1
               print("pdu_gnb_release")
               tr += 1
               file_name = "ue" + ue[0] + ".txt"
               file = open(file_name, "w")
               imsi_value = imsi + ue[0]
               file.write(imsi_value+ "," + str(tr) + "\n")
               file.close()
               p = Process(target=run_command, args=(['bash', './pdu_gnb_release.sh', ue[0]],))
               processes.append(p)
               continue
            except:
               print("error in pdu_gnb_release")    
         case 10:
            try:        
               cd += 1
               print("deregistration")
               tr += 1
               file_name = "ue" + ue[0] + ".txt"
               file = open(file_name, "w")
               imsi_value = imsi + ue[0]
               file.write(imsi_value+ "," + str(tr) + "\n")
               file.close()
               p = Process(target=run_command, args=(['bash', './deregister.sh', ue[0]],))
               processes.append(p)
               continue
            except:
               print("error in deregistration")  
    for p in processes:
       p.start()


    time.sleep(2)
    t += 2
