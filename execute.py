# import time
# import subprocess
# from multiprocessing import Process

# imsi = 'imsi-208930000000'

# number_of_registrations = 0
# number_of_uplinks = 0
# number_of_downlinks = 0
# number_of_ue_releases = 0
# number_of_gnb_releases = 0
# number_of_deregistrations = 0
# error_count = 0

# time_variable = 0 
# #gnb_id_counter = 2

# ue_list = []
# #gnb_ueID_map = {}  #to store gnb id

# # Reading events from the file
# with open("/ueransim/benign_list_40ues_5.0s_8events", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         x = line.strip().split(",", 4)
#         ue_list.append(x)

# def run_command(command):
#     try:
#         subprocess.run(command, check=True)  # Raise an exception for non-zero exit codes
#     except subprocess.CalledProcessError as e:
#         #print(f"Error occurred while running command: {e.cmd}. Return code: {e.returncode}")
#         error_count += 1  # Increment the error count
#     except Exception as e:
#         #print(f"Unexpected error while running command: {command}. Error: {e}")
#         error_count += 1  


# while time_variable <= 2150:
#     t_plus2 = time_variable + 2
#     print("interval in seconds = [", str(time_variable), ", ", str(t_plus2), "]")

   
#     ue_events = [ue for ue in ue_list if time_variable <= float(ue[2]) < t_plus2]

#     ue_events.sort(key=lambda x: float(x[2]))

#     processes = []

#     for ue in ue_events:
#         event = ue[1]
#         imsi_value = imsi + ue[0]
#         event_time = float(ue[2])

#         try:
#             if event == "register":
#                 number_of_registrations += 1
#                 #gnb_id_counter += 1
#                 #gnb_ueID_map[ue[0]] = str(tr)
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/register.sh', ue[0]], ))
#             elif event == "uplink_google":
#                 number_of_uplinks += 1
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/uplink_google.sh', imsi_value], ))
#             elif event == "uplink_text":
#                 number_of_uplinks += 1
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/uplink_text.sh', imsi_value], ))
#             elif event == "uplink_banking":
#                 number_of_uplinks += 1
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/uplink_video.sh', imsi_value], ))
#             elif event == "uplink_video":
#                 number_of_uplinks += 1
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/uplink_video.sh', imsi_value], ))
#             elif event == "downlink":
#                 number_of_downlinks += 1
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/downlink.sh', imsi_value], ))
#             elif event == "ue_release":
#                 number_of_ue_releases += 1
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/pdu_ue_release.sh', imsi_value], ))
#             elif event == "gnb_release":
#                 number_of_gnb_releases += 1
#                 #ue_id = gnb_ueID_map[ue[0]]
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/pdu_gnb_release.sh', imsi_value, ue[0]], ))
#             else:
#                 number_of_deregistrations += 1
#                 p = Process(target=run_command, args=(['bash', '/ueransim/scripts/deregister.sh', imsi_value], ))
            
#             processes.append(p)
#         except KeyError as ke:
#             print(f"KeyError: {ke}")
#         except Exception as e:
#             print(f"Unexpected error: {e}")

#     for p in processes:
#         p.start()

#     time.sleep(2)
    
#     time_variable += 2


# print("number of registerions:" + str(number_of_registrations) + "   number_of_uplinks:" + str(number_of_uplinks) + "   number_of_downlinks" + str(number_of_downlinks) + "   number_of_ue_releases:" + str(number_of_ue_releases) + "   number_of_gnb_releases:" + str(number_of_gnb_releases) + "   number_of_deregistrations:" + str(number_of_deregistrations) + " total number of errors: "+str(error_count))