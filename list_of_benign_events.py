from ue_yaml_file_handling import *
from constants import *
from numpy import random
import math
from time_for_event_execution import *
from list_of_events_per_ue import *

def list_of_benign_events():

    yamlfiles(NUMBER_OF_UES_PER_SLICE, 1, 2, 1) #creates the yaml files for the UEs of slice 1
    yamlfiles(NUMBER_OF_UES_PER_SLICE, 2, 3, 2) #creates the yaml files for the UEs of slice 2
    
    ue_state = dict() #to manage ue states throughout the program (ACTIVE OR DEACTIVATED)
    ues_list = [] #to hold all the UEs in the network!
    ue_selected = [] #to control the number of ues that has been selected
    list_to_execute = []
    active_ues_in_the_next_slot = []
    slot_time = 0.0
    for lambda_value in LIST_OF_LAMBDAS:
      number_of_ues_for_this_lambda = lambda_value * INTERVAL_TIME
      counter = 0
    
      if (lambda_value > 1):
        active_ues_in_the_next_slot = [ue_temp for ue_temp in ue_selected if ue_state[ue_temp + "_D"] >= slot_time] 
        ue_selected.clear()
        ue_selected = active_ues_in_the_next_slot.copy()
      
      ues_list = combined_ue_pool(0, NUMBER_OF_UES_PER_SLICE) #cause we need all of them in the benign attack 
      while (counter < 2):
          print(ues_list)
          selected_ue = random.choice(ues_list)
          ues_list.remove(selected_ue)
          if selected_ue in ue_selected: #ensuring ues are not repeated
            continue
          else: 
            ue_selected.append(selected_ue)
            ue_state[selected_ue + "_A"] = - (1/lambda_value) * math.log(random.random()) + slot_time 
            ue_state[selected_ue + "_D"] = ue_state[selected_ue + "_A"] + service_time()    
            
            lisrt = list_of_events_per_ue(selected_ue, ue_state[selected_ue + "_A"], ue_state[selected_ue + "_D"],
                       LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT, PRBABILITIES_OF_LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_BENIGN,
                       list_to_execute, lambda_value, counter)
            counter+=1 #counting number of selected UEs
      slot_time += INTERVAL_TIME 

    list_to_execute.sort(key = takefourth)

    with open('./benign_events', 'w') as file:
        for line in list_to_execute:
          file.write(','.join(str(item) for item in line))
          file.write("\n" )
          
    return list_to_execute
      

#this function combines all UEs from all slices in the network into ue_list 
def combined_ue_pool(start, end): 
    ues_list = []
    for slice_number in range(1, 3):  # slice1 and slice2
        for ue_number in range(start, end):
            suffix, ue_name = ue_yaml_file_names(slice_number, ue_number)
            ues_list.append(ue_name)
    random.shuffle(ues_list)
    return ues_list 