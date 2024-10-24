import time
import subprocess
from multiprocessing import Process
import random
from read_ips import *

attack_start_time = 0 #CHANGE 
attack_end_time = 0 #CHANGE 


attack_events = ['/ueransim/scripts/TextClientAttack.sh', '/ueransim/scripts/BankClientAttack.sh']
def run_command(command):
        subprocess.run(command)  


while True: #CHANGE TO END TIME OF ATTACK
    ue_ip_list = read_ips()
    processes = []
    
    print("ATTACK RUNNING...")
    random.shuffle(ue_ip_list)
    for ue in ue_ip_list:
        ue_ip = random.choice(ue_ip_list)
        ue_ip_list.remove(ue)
        ue_attack_event = random.choice(attack_events)
        p = Process(target=run_command, args=(['bash', ue_attack_event, ue_ip], ))
        processes.append(p)

    for p in processes:
        p.start()

