import math
import time
import subprocess
from multiprocessing import Process, Semaphore

imsi1 = 'imsi-208930000000'
imsi2 = 'imsi-20893000000'

cr = 2
cua = 0
cus1 = 0
cus2 = 0
cus1d = 0
cus2d = 0
cdl = 0
cpu = 0
cpg = 0
cdr = 0

t = 0 
tr = 1  

ue_list = []
gnb_ueID_map = {}  # to store gnb id

with open("/home/ubuntu/UERANSIM/ahmad_benign/benign_events", "r") as file:
    lines = file.readlines()
    for line in lines:
        x = line.strip().split(",", 4)
        ue_list.append(x)

def run_command(command):
        subprocess.run(command)

while t <= 7230:
    t_plus3 = t + 3
    print("interval in seconds = [", str(t), ", ", str(t_plus3), "]")
    ue_events = [ue for ue in ue_list if t <= math.floor(float(ue[2])) < t_plus3]
    processes = []

    for ue in ue_events:
        event = ue[1]
        imsi = imsi1 if len(ue[0]) == 3 else imsi2
        imsi_value = imsi + ue[0]

        try:
            if event == "1":
                cr += 1
                gnb_ueID_map[ue[0]] = str(cr)
                tr += 1
                p = Process(target=run_command, args=(['bash', '/home/ubuntu/UERANSIM/ahmad_benign/scripts/register.sh', ue[0]],))
            elif event == "2":
                cua += 1
                tr += 1
                p = Process(target=run_command, args=(['bash', '/home/ubuntu/UERANSIM/ahmad_benign/scripts/uplink_any.sh', imsi_value],))
            elif event == "3":
                cus1 += 1
                p = Process(target=run_command, args=(['bash', '/home/ubuntu/UERANSIM/ahmad_benign/scripts/uplink_service1_benign.sh', imsi_value],))
            elif event == "4":
                cus2 += 1
                p = Process(target=run_command, args=(['bash', '/home/ubuntu/UERANSIM/ahmad_benign/scripts/uplink_service2_benign.sh', imsi_value],))
            elif event == "5":
                cus1d += 1
                p = Process(target=run_command, args=(['bash', '/home/ubuntu/UERANSIM/ahmad_benign/scripts/uplink_service1_delayed.sh', imsi_value],))
            elif event == "6":
                cus2d += 1
                p = Process(target=run_command, args=(['bash', '/home/ubuntu/UERANSIM/ahmad_benign/scripts/uplink_service2_delayed.sh', imsi_value],))
            elif event == "7":
                cdl += 1
                p = Process(target=run_command, args=(['bash', '/home/ubuntu/UERANSIM/ahmad_benign/scripts/downlink.sh', imsi_value],))
            elif event == "8":
                cpu += 1
                p = Process(target=run_command, args=(['bash', '/home/ubuntu/UERANSIM/ahmad_benign/scripts/pdu_ue_release.sh', imsi_value],))
            elif event == "9":
                cpg += 1
                ue_id = gnb_ueID_map[ue[0]]
                p = Process(target=run_command, args=(['bash', '/home/ubuntu/UERANSIM/ahmad_benign/scripts/pdu_gnb_release.sh', imsi_value, ue_id],))
            else:
                cdr += 1
                p = Process(target=run_command, args=(['bash', '/home/ubuntu/UERANSIM/ahmad_benign/scripts/deregister.sh', imsi_value],))
            processes.append(p)
        except KeyError as ke:
            print(f"KeyError: {ke}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    for p in processes:
        p.start()

    # Allow some time for the started processes to run
    time.sleep(3)
    t += 3

print("cr:" + str(cr) + "   cua:" + str(cua) + "   cus1:" + str(cus1) + "   cus2:" + str(cus2) + "   cus1d:" + str(cus1d) + "   cus2d:" + str(cus2d) + "   cdl:" + str(cdl) + "   cpu:" + str(cpu) + "   cpg:" + str(cpg) + "   cdr:" + str(cdr))
