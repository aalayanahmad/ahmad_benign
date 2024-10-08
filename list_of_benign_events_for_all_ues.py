from ue_yaml_file_handling import *
from ahmad_benign.constants_RN import *
from numpy import random
import math
from time_for_event_execution import *
from ue_poisson_event_distribution import *
import copy

def list_of_benign_events_for_all_ues():

    ue_state = dict() #to manage ue states throughout the program (ACTIVE OR DEACTIVATED)
    complete_ues_list = [] #to hold all the UEs in the network!
    selected_ues = [] #to hold the ues that has been selected and "1" if it is anythin other than deregisteration, "0" otherwise
    list_to_execute = []
    active_ues_from_previous_slot = []
    slot_time = 0.0
    for lambda_value in LIST_OF_LAMBDAS:
      #########################################################################################
      number_of_ues_for_this_lambda = lambda_value * INTERVAL_TIME 
      counter = 0
      complete_ues_list = combined_ue_pool(0, NUMBER_OF_UES_PER_SLICE) #cause all of them will be performing benign procedures (need not exclude anything as attack)
      #########################################################################################
      if lambda_value > 1:
        active_ues_from_previous_slot = [ue for ue in selected_ues if ue_state[ue +"_depart"] >= slot_time] #check ues that will still be active when this slot starts
        selected_ues.clear() #to choose a new set of UEs for the next lambda 
        selected_ues = copy.deepcopy(active_ues_from_previous_slot) #put them in selected to avoid repetition
        print("selected ues:" , selected_ues)
      #########################################################################################
      number_of_available_ues = len(complete_ues_list) - len(selected_ues) #if i have 12 ues in total for this lambda and 12 ues in my enitre network, if two of them are in selected ues 
      if(number_of_available_ues >= number_of_ues_for_this_lambda):
          complete_ues_list = [ue for ue in complete_ues_list if ue not in selected_ues] #to make sure im never choosing an already selected ue
      else:
          complete_ues_list = [ue for ue in complete_ues_list if ue not in selected_ues]
          number_of_ues_for_this_lambda = number_of_available_ues
      #########################################################################################
      while (counter < number_of_ues_for_this_lambda):
            selected_ue = random.choice(complete_ues_list)
            complete_ues_list.remove(selected_ue)
            selected_ues.append(selected_ue)
            ue_state[selected_ue + "_arrive"] = (-(1/lambda_value) * math.log(random.random())) + slot_time #poisson arrival of ues
            ue_state[selected_ue + "_depart"] = ue_state[selected_ue + "_arrive"] + (service_time())   #serive time acc to formula t_departure = t_arrival + service time   
            print(selected_ue, "will be active form: ", ue_state[selected_ue + "_arrive"]*60, " until ", ue_state[selected_ue + "_depart"]*60)
            ue_poisson_event_distribution(selected_ue, ue_state[selected_ue + "_arrive"]*60, ue_state[selected_ue + "_depart"]*60, list_to_execute, lambda_value)
            counter += 1 #counting number of selected UEs
      #########################################################################################      
      slot_time += INTERVAL_TIME #move to the next slot time (i.e next lambda) 

    list_to_execute.sort(key = take_fourth)
    with open(f"./files_to_execute/benign_list_{NUMBER_OF_UES_PER_SLICE}ues_{INTERVAL_TIME}s_{EVENTS_PER_MINUTE}events_me", 'w') as file:
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