from ue_yaml_file_handling import *
from constants import *
from numpy import random
import math
from time_for_event_execution import *
from ue_poisson_event_distribution import *

def list_of_benign_events_for_all_ues():

    ue_state = dict() #to manage ue states throughout the program (ACTIVE OR DEACTIVATED)
    complete_ues_list = [] #to hold all the UEs in the network!
    selected_ues = [] #to hold the ues that has been selected
    list_to_execute = []
    ues_that_will_still_be_active_in_the_next_slot = []
    slot_time = 0.0
    for lambda_value in LIST_OF_LAMBDAS:
      #use a different seed per lambda
      random_seed = random.randint(0, 10000)  
      random.seed(random_seed)
      number_of_ues_for_this_lambda = lambda_value * INTERVAL_TIME #why ASK
      counter = 0
    
      if (lambda_value > 1):
        selected_ues.clear()
        ues_that_will_still_be_active_in_the_next_slot = [ue_temp for ue_temp in selected_ues if ue_state[ue_temp + "_depart"] >= slot_time] 
        #to ensure these ues are not selected while they are still active
        selected_ues = ues_that_will_still_be_active_in_the_next_slot.copy()
      
      complete_ues_list = combined_ue_pool(0, NUMBER_OF_UES_PER_SLICE) #cause all of them will be performing benign procedures (need not exclude anything as attack)
      while (counter < number_of_ues_for_this_lambda):
          selected_ue = random.choice(complete_ues_list)
          complete_ues_list.remove(selected_ue)
          if selected_ue in selected_ues: #ensuring ues are not repeated
            continue
          else: 
            selected_ues.append(selected_ue)
            ue_state[selected_ue + "_arrive"] = (-(1/lambda_value) * math.log(random.random())) + slot_time #poisson arrival of ues
            ue_state[selected_ue + "_depart"] = ue_state[selected_ue + "_arrive"] + service_time() #serive time acc to formula t_departure = t_arrival + service time   
            
            ue_poisson_event_distribution(selected_ue, ue_state[selected_ue + "_arrive"], ue_state[selected_ue + "_depart"], list_to_execute, lambda_value, counter)
            counter+=1 #counting number of selected UEs
      slot_time += INTERVAL_TIME #move to the next slot time (i.e next lambda) 

    list_to_execute.sort(key = takefourth)

    with open('./list_of_benign_events_for_all_ues', 'w') as file:
        for line in list_to_execute:
          file.write(','.join(str(item) for item in line))
          file.write("\n" )
          
    return list_to_execute
#what happens if the next event was de registration??? i de register twice      

#this function combines all UEs from all slices in the network into ue_list 
def combined_ue_pool(start, end): 
    ues_list = []
    for slice_number in range(1, 3):  # slice1 and slice2
        for ue_number in range(start, end):
            suffix, ue_name = ue_yaml_file_names(slice_number, ue_number)
            ues_list.append(ue_name)
    random.shuffle(ues_list)
    return ues_list 