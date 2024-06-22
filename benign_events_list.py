from ue_yaml_file_handling import *
from constants import *
from numpy import random
import math
from time_for_event_execution import *
from list_event import *

def benign_events_list():

    yamlfiles(NUMBER_OF_UES_PER_SLICE, 1, 2, 1) #creates the yaml files for the UEs of slice 1
    yamlfiles(NUMBER_OF_UES_PER_SLICE, 2, 3, 2) #creates the yaml files for the UEs of slice 2
    
    ue_state = dict() #to manage the different ue states throughout the program
    ues_list = [] #to hold all the UEs in the network!
    ue_selected = [] #to control the number of ues that has been selected.
    list_to_execute = []
    temp_ue_list = []
 
    slot_time = 0.0

    for lambda_value in LIST_OF_LAMBDAS:
      number_of_ues_for_this_lambda = lambda_value * INTERVAL_TIME
      counter = 1
      if (lambda_value > 1):
        temp_ue_list = [ue_temp for ue_temp in ue_selected if ue_state[ue_temp + "_D"] >= slot_time] #deregister? ASK
        ue_selected.clear()
        ue_selected = temp_ue_list.copy()
        ues_list = combined_ue_pool(0, NUMBER_OF_UES_PER_SLICE) #cause we need all of them in the benign attack
        while counter <= number_of_ues_for_this_lambda:
          selected_ue = random.choice(ues_list)
          if selected_ue in ue_selected: #checking that ues are not repeated
            continue
          else: 
            ue_selected.append(selected_ue)
            ue_state[selected_ue + "_A"] = - (1/lambda_value) * math.log(random.rand()) + slot_time 
            ue_state[selected_ue + "_D"] = ue_state[selected_ue + "_A"] + service_time()    
            
            list_event(selected_ue, ue_state[selected_ue + "_A"], ue_state[selected_ue + "_D"],
                       REGISTER, UPLINK_ANY, UPLINK_SERVICE1, UPLINK_SERVICE2, UPLINK_SERVICE1_DELAYED, 
                       UPLINK_SERVICE2_DELAYED, DOWNLINK, PDU_UE_RELEASE, PDU_GNB_RELEASE, IDLE, 
                       PB_REGISTER, PB_UPLINK_ANY, PB_UPLINK_SERVICE1, PB_UPLINK_SERVICE2,
                       PB_UPLINK_SERVICE1_DELAYED, PB_UPLINK_SERVICE2_DELAYED, 
                       PB_DOWNLINK, PB_PDU_UE_RELEASE, PB_PDU_GNB_RELEASE, PB_IDLE,
                       list_to_execute,lambda_value, counter) #sending the ue's state, and configuration accordingly to first scenarios(it is done for the 3 attack and normal behavior)
            counter+=1 #counting number of selected UEs
            slot_time += INTERVAL_TIME 

        list_to_execute.sort(key = takefourth)

        with open('/home/ubuntu/UERANSIM/script/files/BeningList_attack1.txt', 'w') as file:
          for line in list_to_execute:
            file.write(','.join(str(item) for item in line))
            file.write("\n" )

        for i in list_to_execute:
          print(i)
          
        return list_to_execute
      

#this function combines all UEs from all slices in the network into the ue_list! 
def combined_ue_pool(start, end): 
 ues_list = []
 for slice_number in range(1,3): #slice1 and slice2
  for ue_number in range (start, end):
   ue_name = ue_yaml_file_names(slice_number, ue_number)
   ues_list.append(ue_name)
  random.shuffle(ues_list)
  return ues_list   
