from random_event_selection import random_next_event_selection
from constants import EVENTS_PER_MINUTE
from time_for_event_execution import time_execution_current_event
import math
import random

def list_of_events_per_ue(selected_ue, start, end, legal_next_events_per_current_event, probabilities_of_legal_next_events_per_current_event_benign, list_to_store_events, lambda_value, logging_index):
    
    print(f"{logging_index}) {selected_ue} init: {start} ({start * 60}) end: {end} ({end * 60}) lambda: {lambda_value}")

    end_in_seconds = end * 60  
    list_to_store_events.append([int(selected_ue[2:5]), 1, start * 60, lambda_value]) #TO DO

    current_state = 1  # start with registration state
    time = start * 60 
    attempts = 0
    p = 0

    while (time <= (end_in_seconds - 10)): 
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
            if (p <= (end_in_seconds - 10)):  
                time = p
                list_to_store_events.append([int(selected_ue[2:5]), event_to_trigger, time, lambda_value])
                current_state = event_to_trigger
            else:
                c += 1

    # Append the final deregister event
    list_to_store_events.append([int(selected_ue[2:5]), 12, end * 60, lambda_value])

    return list_to_store_events
