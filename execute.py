import math
import time
import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

imsi1 = 'imsi-208930000000'
imsi2 = 'imsi-20893000000'
cr = 2
cua = 0
cus1 = 0
cus2 = 0
cus1d = 0
cus2d = 0
cd = 0
cpu = 0
cpg = 0
cd = 0

t = 0  # Start time
tr = 1  # Transaction ID

ue_list = []
with open("/ueransim/benign_events", "r") as file:
    lines = file.readlines()
    for line in lines:
        x = line.strip().split(",", 4)
        ue_list.append(x)


def run_command(command):
    subprocess.run(command)


counter_map = {}


def process_ue_event(ue, t):
    global tr, cr, cua, cus1, cus2, cus1d, cus2d, cd, counter_map
    event_type = ue[1]
    try:
        if event_type == "1":
            cr += 1
            print("registration")
            counter_map[ue[0]] = cr
            tr += 1
            file_name = "ue" + ue[0] + ".yaml"
            with open(file_name, "w") as file:
                imsi = imsi1 if len(ue[0]) == 3 else imsi2
                imsi_value = imsi + ue[0]
                file.write(imsi_value + "," + str(tr) + "\n")
            run_command(['bash', '/ueransim/scripts/register.sh', file_name])

        elif event_type == "2":
            cua += 1
            print("uplink_any")
            tr += 1
            file_name = "ue" + ue[0] + ".txt"
            with open(file_name, "w") as file:
                imsi = imsi1 if len(ue[0]) == 3 else imsi2
                imsi_value = imsi + ue[0]
                file.write(imsi_value + "," + str(tr) + "\n")
            run_command(['bash', '/ueransim/scripts/uplink_any.sh', imsi_value])

        elif event_type == "3":
            cus1 += 1
            print("uplink_service1")
            tr += 1
            file_name = "ue" + ue[0] + ".txt"
            with open(file_name, "w") as file:
                imsi = imsi1 if len(ue[0]) == 3 else imsi2
                imsi_value = imsi + ue[0]
                file.write(imsi_value + "," + str(tr) + "\n")
            run_command(['bash', '/ueransim/scripts/uplink_service1_benign.sh', imsi_value])

        elif event_type == "4":
            cus2 += 1
            print("uplink_service2")
            tr += 1
            file_name = "ue" + ue[0] + ".txt"
            with open(file_name, "w") as file:
                imsi = imsi1 if len(ue[0]) == 3 else imsi2
                imsi_value = imsi + ue[0]
                file.write(imsi_value + "," + str(tr) + "\n")
            run_command(['bash', '/ueransim/scripts/uplink_service2_benign.sh', imsi_value])

        elif event_type == "5":
            cus1d += 1
            print("uplink_service1_delayed")
            tr += 1
            file_name = "ue" + ue[0] + ".txt"
            with open(file_name, "w") as file:
                imsi = imsi1 if len(ue[0]) == 3 else imsi2
                imsi_value = imsi + ue[0]
                file.write(imsi_value + "," + str(tr) + "\n")
            run_command(['bash', '/ueransim/scripts/uplink_service1_delayed.sh', imsi_value])

        elif event_type == "6":
            cus2d += 1
            print("uplink_service2_delayed")
            tr += 1
            file_name = "ue" + ue[0] + ".txt"
            with open(file_name, "w") as file:
                imsi = imsi1 if len(ue[0]) == 3 else imsi2
                imsi_value = imsi + ue[0]
                file.write(imsi_value + "," + str(tr) + "\n")
            run_command(['bash', '/ueransim/scripts/uplink_service2_delayed.sh', imsi_value])

        elif event_type == "7":
            cd += 1
            print("downlink")
            tr += 1
            file_name = "ue" + ue[0] + ".txt"
            with open(file_name, "w") as file:
                imsi = imsi1 if len(ue[0]) == 3 else imsi2
                imsi_value = imsi + ue[0]
                file.write(imsi_value + "," + str(tr) + "\n")
            run_command(['bash', '/ueransim/scripts/downlink.sh', imsi_value])

        elif event_type == "8":
            cd += 1
            print("pdu_ue_release")
            tr += 1
            file_name = "ue" + ue[0] + ".txt"
            with open(file_name, "w") as file:
                imsi = imsi1 if len(ue[0]) == 3 else imsi2
                imsi_value = imsi + ue[0]
                file.write(imsi_value + "," + str(tr) + "\n")
            run_command(['bash', '/ueransim/scripts/pdu_ue_release.sh', imsi_value])

        elif event_type == "9":
            cd += 1
            print("pdu_gnb_release")
            tr += 1
            file_name = "ue" + ue[0] + ".txt"
            with open(file_name, "w") as file:
                imsi = imsi1 if len(ue[0]) == 3 else imsi2
                imsi_value = imsi + ue[0]
                file.write(imsi_value + "," + str(tr) + "\n")
            run_command(['bash', '/ueransim/scripts/pdu_gnb_release.sh', imsi_value, str(counter_map[ue[0]])])

        elif event_type == "10":
            cd += 1
            print("deregistration")
            tr += 1
            file_name = "ue" + ue[0] + ".txt"
            with open(file_name, "w") as file:
                imsi = imsi1 if len(ue[0]) == 3 else imsi2
                imsi_value = imsi + ue[0]
                file.write(imsi_value + "," + str(tr) + "\n")
            run_command(['bash', '/ueransim/scripts/deregister.sh', imsi_value])
    except Exception as e:
        print(f"Error processing UE {ue[0]} event type {event_type}: {e}")


def main():
    global t
    max_workers = multiprocessing.cpu_count()  # Use all available CPUs
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        while t <= 7230:
            t_plus4 = t + 4
            print("interval in seconds = [", str(t), ", ", str(t + 4), "]")
            ue_events = [ue for ue in ue_list if t <= math.floor(float(ue[2])) < t_plus4]
            future_to_ue = {executor.submit(process_ue_event, ue, t): ue for ue in ue_events}
            for future in as_completed(future_to_ue):
                try:
                    future.result()
                except Exception as exc:
                    ue = future_to_ue[future]
                    print(f"UE {ue[0]} generated an exception: {exc}")
            time.sleep(4)
            t += 4


if __name__ == '__main__':
    main()
