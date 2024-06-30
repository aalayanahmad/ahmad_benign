# import math
# import time
# import subprocess
# from multiprocessing import Process

# imsi1 = 'imsi-208930000000' 
# imsi2 = 'imsi-20893000000' 
# cr = 0
# cua = 0
# cus1 = 0
# cus2 = 0
# cus1d = 0
# cus2d = 0
# cd = 0
# cpu = 0
# cpg = 0
# cd = 0  

# t = 0  # Start time
# tr = 1  # Transaction ID

# ue_list = []
# with open("/ueransim/benign_events", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         x = line.strip().split(",", 4)
#         ue_list.append(x)


# def run_command(command):
#     subprocess.run(command)

# def process_list_of_ue_events(ue_events, t):
#     global tr, cr, cua, cus1, cus2, cus1d, cus2d, cd
#     processes = []
#     for ue in ue_events:
#         event_type = ue[1]
#         if event_type == "1":
#             try:
#                 cr += 1
#                 print("registration")
#                 tr += 1
#                 file_name = "ue" + ue[0] + ".yaml"
#                 with open(file_name, "w") as file:
#                     imsi = imsi1 if len(ue[0]) == 3 else imsi2
#                     imsi_value = imsi + ue[0]
#                     file.write(imsi_value + "," + str(tr) + "\n")
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/register.sh', file_name],))
#                 processes.append(p)
#             except Exception as e:
#                 print(f"Error in registration: {e}")
        
#         elif event_type == "2":
#             try:        
#                 cua += 1
#                 print("uplink_any")
#                 tr += 1
#                 file_name = "ue" + ue[0] + ".txt"
#                 with open(file_name, "w") as file:
#                     imsi = imsi1 if len(ue[0]) == 3 else imsi2
#                     imsi_value = imsi + ue[0]
#                     file.write(imsi_value + "," + str(tr) + "\n")
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/uplink_any.sh', imsi_value],))
#                 processes.append(p)
#             except Exception as e:
#                 print(f"Error in uplink_any: {e}")
        
#         elif event_type == "3":
#             try:        
#                 cus1 += 1
#                 print("uplink_service1")
#                 tr += 1
#                 file_name = "ue" + ue[0] + ".txt"
#                 with open(file_name, "w") as file:
#                     imsi = imsi1 if len(ue[0]) == 3 else imsi2
#                     imsi_value = imsi + ue[0]
#                     file.write(imsi_value + "," + str(tr) + "\n")
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/uplink_service1_benign.sh', imsi_value],))
#                 processes.append(p)
#             except Exception as e:
#                 print(f"Error in uplink_service1: {e}")
        
#         elif event_type == "4":
#             try:        
#                 cus2 += 1
#                 print("uplink_service2")
#                 tr += 1
#                 file_name = "ue" + ue[0] + ".txt"
#                 with open(file_name, "w") as file:
#                     imsi = imsi1 if len(ue[0]) == 3 else imsi2
#                     imsi_value = imsi + ue[0]
#                     file.write(imsi_value + "," + str(tr) + "\n")
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/uplink_service2_benign.sh', imsi_value],))
#                 processes.append(p)
#             except Exception as e:
#                 print(f"Error in uplink_service2: {e}")
        
#         elif event_type == "5":
#             try:        
#                 cus1d += 1
#                 print("uplink_service1_delayed")
#                 tr += 1
#                 file_name = "ue" + ue[0] + ".txt"
#                 with open(file_name, "w") as file:
#                     imsi = imsi1 if len(ue[0]) == 3 else imsi2
#                     imsi_value = imsi + ue[0]
#                     file.write(imsi_value + "," + str(tr) + "\n")
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/uplink_service1_delayed.sh', imsi_value],))
#                 processes.append(p)
#             except Exception as e:
#                 print(f"Error in uplink_service1_delayed: {e}")
        
#         elif event_type == "6":
#             try:        
#                 cus2d += 1
#                 print("uplink_service2_delayed")
#                 tr += 1
#                 file_name = "ue" + ue[0] + ".txt"
#                 with open(file_name, "w") as file:
#                     imsi = imsi1 if len(ue[0]) == 3 else imsi2
#                     imsi_value = imsi + ue[0]
#                     file.write(imsi_value + "," + str(tr) + "\n")
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/uplink_service2_delayed.sh', imsi_value],))
#                 processes.append(p)
#             except Exception as e:
#                 print(f"Error in uplink_service2_delayed: {e}")
        
#         elif event_type == "7":
#             try:        
#                 cd += 1
#                 print("downlink")
#                 tr += 1
#                 file_name = "ue" + ue[0] + ".txt"
#                 with open(file_name, "w") as file:
#                     imsi = imsi1 if len(ue[0]) == 3 else imsi2
#                     imsi_value = imsi + ue[0]
#                     file.write(imsi_value + "," + str(tr) + "\n")
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/downlink.sh', imsi_value],))
#                 processes.append(p)
#             except Exception as e:
#                 print(f"Error in downlink: {e}")
        
#         elif event_type == "8":
#             try:        
#                 cd += 1
#                 print("pdu_ue_release")
#                 tr += 1
#                 file_name = "ue" + ue[0] + ".txt"
#                 with open(file_name, "w") as file:
#                     imsi = imsi1 if len(ue[0]) == 3 else imsi2
#                     imsi_value = imsi + ue[0]
#                     file.write(imsi_value + "," + str(tr) + "\n")
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/pdu_ue_release.sh', imsi_value],))
#                 processes.append(p)
#             except Exception as e:
#                 print(f"Error in pdu_ue_release: {e}")
        
#         elif event_type == "9":
#             try:        
#                 cd += 1
#                 print("pdu_gnb_release")
#                 tr += 1
#                 file_name = "ue" + ue[0] + ".txt"
#                 with open(file_name, "w") as file:
#                     imsi = imsi1 if len(ue[0]) == 3 else imsi2
#                     imsi_value = imsi + ue[0]
#                     file.write(imsi_value + "," + str(tr) + "\n")
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/pdu_gnb_release.sh', imsi_value, ue[0]],))
#                 processes.append(p)
#             except Exception as e:
#                 print(f"Error in pdu_gnb_release: {e}")
        
#         elif event_type == "10":
#             try:        
#                 cd += 1
#                 print("deregistration")
#                 tr += 1
#                 file_name = "ue" + ue[0] + ".txt"
#                 with open(file_name, "w") as file:
#                     imsi = imsi1 if len(ue[0]) == 3 else imsi2
#                     imsi_value = imsi + ue[0]
#                     file.write(imsi_value + "," + str(tr) + "\n")
#                 p = Process(target=run_command, args=(['bash', '/ueransimn/scripts/deregister.sh', imsi_value],))
#                 processes.append(p)
#             except Exception as e:
#                 print(f"Error in deregistration: {e}")
    
#     for p in processes:
#         p.start()

# def main():
#     global t
#     while t <= 7230: 
#         t_plus2 = t + 2
#         print("interval in seconds = [", str(t), ", ", str(t + 2) , "]")
#         ue_events = [ue for ue in ue_list if t <= math.floor(float(ue[2])) < t_plus2]
#         process_list_of_ue_events(ue_events, t)
#         time.sleep(2)
#         t += 2

# if __name__ == '__main__':
#     main()
