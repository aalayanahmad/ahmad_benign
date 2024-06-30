import math
import time
import subprocess
from multiprocessing import Pool, cpu_count

imsi1 = 'imsi-208930000000'
imsi2 = 'imsi-20893000000'
cr = cua = cus1 = cus2 = cus1d = cus2d = cd = cpu = cpg = 0
t = 0  # Start time
tr = 1  # Transaction ID

ue_list = []
with open("'/ueransim/benign_events", "r") as file:
    lines = file.readlines()
    for line in lines:
        x = line.strip().split(",", 4)
        ue_list.append(x)


def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error: {e}")


def process_ue_event(ue, tr):
    global cr, cua, cus1, cus2, cus1d, cus2d, cd
    event_type = ue[1]
    file_name = f"ue{ue[0]}.txt"
    imsi = imsi1 if len(ue[0]) == 3 else imsi2
    imsi_value = imsi + ue[0]

    try:
        if event_type == "1":
            cr += 1
            print("registration")
            tr += 1
            with open(file_name, "w") as file:
                file.write(f"{imsi_value},{tr}\n")
            run_command(['bash', '/ueransim/register.sh', file_name])
        elif event_type == "2":
            cua += 1
            print("uplink_any")
            tr += 1
            with open(file_name, "w") as file:
                file.write(f"{imsi_value},{tr}\n")
            run_command(['bash', '/ueransim/uplink_any.sh', imsi_value])
        elif event_type == "3":
            cus1 += 1
            print("uplink_service1")
            tr += 1
            with open(file_name, "w") as file:
                file.write(f"{imsi_value},{tr}\n")
            run_command(['bash', '/ueransim/uplink_service1_benign.sh', imsi_value])
        elif event_type == "4":
            cus2 += 1
            print("uplink_service2")
            tr += 1
            with open(file_name, "w") as file:
                file.write(f"{imsi_value},{tr}\n")
            run_command(['bash', '/ueransim/uplink_service2_benign.sh', imsi_value])
        elif event_type == "5":
            cus1d += 1
            print("uplink_service1_delayed")
            tr += 1
            with open(file_name, "w") as file:
                file.write(f"{imsi_value},{tr}\n")
            run_command(['bash', '/ueransim/uplink_service1_delayed.sh', imsi_value])
        elif event_type == "6":
            cus2d += 1
            print("uplink_service2_delayed")
            tr += 1
            with open(file_name, "w") as file:
                file.write(f"{imsi_value},{tr}\n")
            run_command(['bash', '/ueransim/uplink_service2_delayed.sh', imsi_value])
        elif event_type == "7":
            cd += 1
            print("downlink")
            tr += 1
            with open(file_name, "w") as file:
                file.write(f"{imsi_value},{tr}\n")
            run_command(['bash', '/ueransim/downlink.sh', imsi_value])
        elif event_type == "8":
            cd += 1
            print("pdu_ue_release")
            tr += 1
            with open(file_name, "w") as file:
                file.write(f"{imsi_value},{tr}\n")
            run_command(['bash', '/ueransim/pdu_ue_release.sh', imsi_value])
        elif event_type == "9":
            cd += 1
            print("pdu_gnb_release")
            tr += 1
            with open(file_name, "w") as file:
                file.write(f"{imsi_value},{tr}\n")
            run_command(['bash', '/ueransim/pdu_gnb_release.sh', imsi_value, ue[0]])
        elif event_type == "10":
            cd += 1
            print("deregistration")
            tr += 1
            with open(file_name, "w") as file:
                file.write(f"{imsi_value},{tr}\n")
            run_command(['bash', '/ueransim/deregister.sh', imsi_value])
    except Exception as e:
        print(f"Error processing event {event_type} for UE {ue[0]}: {e}")


def main():
    global t, tr
    pool_size = min(len(ue_list), cpu_count() * 2)  # Adjust pool size as needed
    with Pool(processes=pool_size) as pool:
        while t <= 7230:
            t_plus2 = t + 2
            print(f"interval in seconds = [{t}, {t_plus2}]")
            ue_events = [ue for ue in ue_list if t <= math.floor(float(ue[2])) < t_plus2]
            for ue in ue_events:
                pool.apply_async(process_ue_event, args=(ue, tr))
            pool.close()
            pool.join()
            time.sleep(2)
            t += 2


if __name__ == '__main__':
    main()
