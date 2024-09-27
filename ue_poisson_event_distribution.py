from random_event_selection import random_next_event_selection
from constants import EVENTS_PER_SECOND
from time_for_event_execution import time_execution_current_event
import math
import random
import re

def ue_poisson_event_distribution(selected_ue, t_arrival, t_departure, list_of_events_for_this_ue, lambda_value, logging_index):
    #logging
    #print(f"{logging_index}) {selected_ue} event starts at: {start} ({start * 60}) and ends at: {end} ({end * 60}) lambda: {lambda_value}")

    #use a different seed per ue
    random_seed = random.randint(0, 10000)  
    random.seed(random_seed)
    
    #the time the UE must DEPART the network (according to service time)
    t_departure = t_departure * 60 
    #the time the UE ARRIVES to the network (according to service time)
    t_arrival = t_arrival * 60
    #appending the REGISTER event as the first one accoridng to UE poisson arrival time
    list_of_events_for_this_ue.append([int(selected_ue[2:5]), 1, t_arrival, lambda_value]) 
    #need to go from REGISTER to another event so set current state to REGISTER
    current_state = 1  
    #the poisson arrivals formula is: t_i = t_(i-1) + poisson, so set t(i-1) to arrival time t0 because t1 = t0 + poisson 
    t_previous = t_arrival #initially t_0 = time of arrival of this specific UE in seconds (according to service time)
    t_current = 0 #this is the time at which the next event is gonna start
    #to check if any other event is allowed before ending the UEs services, check else below to understand
    attempts = 0

    while (t_previous <= (t_departure - 10)): 
        if (attempts == 4):
            break
        else:
            #generate the time until next event of this UE using a poisson distribution
            inter_arrival_time = (-(1/EVENTS_PER_SECOND) * math.log(random.random())) #delta or poisson in: t_i = t_(i+1) + delta
            current_event_execution_time = time_execution_current_event(current_state)
            next_event_to_trigger = random_next_event_selection(current_state)

            #determine if the calculated time will interfere with the time of the previous event (ensure current event finishes execution before moving to the next event)
            if (math.floor(inter_arrival_time) < current_event_execution_time):
                t_current = t_previous + current_event_execution_time 
            else:
                t_current = t_previous + inter_arrival_time #t_i = t_(i+1) + delta
            
            #check if the ue is still within its allowed service time
            if (t_current <= (t_departure - 10)):  
                t_previous = t_current
                #append this event
                list_of_events_for_this_ue.append([extract_ue_number(selected_ue), next_event_to_trigger, t_previous, lambda_value])
                #move to the next state
                current_state = next_event_to_trigger
            else: #allow it to try a couple of times
                attempts += 1

    #append the final deregister event
    list_of_events_for_this_ue.append([extract_ue_number(selected_ue), 6, t_departure, lambda_value])

    return list_of_events_for_this_ue



def extract_ue_number(file_name):
    match = re.search(r"ue(\d+)\.yaml", file_name)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid filename format")
    