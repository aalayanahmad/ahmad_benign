from random_event_selection import random_event_selection
from constants import EVENTS_PER_MINUTE
from time_for_event_execution import time_execution_current_event
import math
import random

def list_event(selected_ue, start, end,
              register, uplink_any, uplink_service1, uplink_service2, 
              uplink_service1_with_network_issues, uplink_service2_with_network_issues, 
              downlink, pdu_ue_release, pdu_gnb_release, idle, 
              probability_register, probability_uplink_any, probability_uplink_service1, 
              probability_uplink_service2, probability_uplink_service1_with_network_issues, 
              probability_uplink_service2_with_network_issues, probability_downlink, 
              probability_pdu_ue_release, probability_pdu_gnb_release, probability_idle,
              arr, lambda_value, i):

    print(f"{i}) {selected_ue} init: {start} ({start * 60}) end: {end} ({end * 60}) lambda: {lambda_value}")

    end_in_seconds = end * 60  # convert minutes to seconds
    arr.append([int(selected_ue[2:5]), 1, start * 60, lambda_value])  # 0 = deregister, 1 = register

    current_state = 1  # start with registration state
    time = start * 60  # start time in seconds
    c = 0

    while time <= (end_in_seconds - 10):  # 10 seconds guard time
        # Select the next event based on current state
        event_to_trigger = random_event_selection(current_state, register, uplink_any, uplink_service1, 
                                                  uplink_service2, uplink_service1_with_network_issues, 
                                                  uplink_service2_with_network_issues, downlink, pdu_ue_release, 
                                                  pdu_gnb_release, idle, probability_register, probability_uplink_any, 
                                                  probability_uplink_service1, probability_uplink_service2, 
                                                  probability_uplink_service1_with_network_issues, 
                                                  probability_uplink_service2_with_network_issues, probability_downlink, 
                                                  probability_pdu_ue_release, probability_pdu_gnb_release, probability_idle)
        
        current_event = current_state

        # Generate time until next event using Poisson distribution
        poisson = -(1/EVENTS_PER_MINUTE) * math.log(random.random()) * 60
        
        # Calculate the time to execute the current event
        current_event_execution_time = time_execution_current_event(current_state)

        # Determine the next event trigger time
        if math.floor(poisson) < current_event_execution_time:
            p = time + current_event_execution_time
        else:
            p = time + poisson

        # Check if the next event trigger time is within the allowed time window
        if p <= (end_in_seconds - 10):  # ensure at least 10 seconds before end
            time = p
            arr.append([int(selected_ue[2:5]), event_to_trigger, time, lambda_value])
            current_state = event_to_trigger
        else:
            c += 1
        
        # Break the loop if too many attempts fail
        if c == 3:
            break

    # Append the final deregister event
    arr.append([int(selected_ue[2:5]), 0, end * 60, lambda_value])

    return arr
