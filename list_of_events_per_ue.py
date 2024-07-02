from random_event_selection import random_next_event_selection
from constants import EVENTS_PER_MINUTE
from time_for_event_execution import time_execution_current_event
import math
import random
import re

def list_of_events_per_ue(selected_ue, start, end, legal_next_events_per_current_event, probabilities_of_legal_next_events_per_current_event_benign, list_to_store_events, lambda_value, logging_index):
    
    print(f"{logging_index}) {selected_ue} event starts at: {start} ({start * 60}) and ends at: {end} ({end * 60}) lambda: {lambda_value}")

    end_in_seconds = end * 60  
    list_to_store_events.append([int(selected_ue[2:5]), 1, start * 60, lambda_value]) 

    current_state = 1  # start with registration state
    time = start * 60 
    attempts = 0
    p = 0
    while (time <= (end_in_seconds - 25)): 
        if (attempts == 3):
            break
        else:
            event_to_trigger = random_next_event_selection(current_state, legal_next_events_per_current_event, probabilities_of_legal_next_events_per_current_event_benign)
            # generate the time until next event using a poisson distribution
            poisson = -(1/EVENTS_PER_MINUTE) * math.log(random.random()) * 60

            current_event_execution_time = time_execution_current_event(current_state)

            # Determine if the calculated time is sufficient for the event to xomplete execution
            if (math.floor(poisson) < current_event_execution_time):
                p = time + current_event_execution_time
            else:
                p = time + poisson

            # Check if the next event trigger time is within the allowed time window
            if (p <= (end_in_seconds - 25)):  
                time = p
                list_to_store_events.append([extract_ue_number(selected_ue), event_to_trigger, time, lambda_value])
                current_state = event_to_trigger
            else:
                attempts += 1

    # Append the final deregister event
    list_to_store_events.append([extract_ue_number(selected_ue), 10, end * 60, lambda_value])

    return list_to_store_events



def extract_ue_number(file_name):
    match = re.search(r"ue(\d+)\.yaml", file_name)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid filename format")
    