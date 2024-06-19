from numpy import random

def random_event_selection(current_state, register, uplink_service1, uplink_service2, 
                           uplink_service1_with_network_issues, uplink_service2_with_network_issues, 
                           downlink, pdu_s_release, idle, p_register, p_uplink_service1, p_uplink_service2, 
                           p_uplink_service1_with_network_issues, p_uplink_service2_with_network_issues, p_downlink, 
                           p_pdu_s_release, p_idle):
    
    deregister = [1] #as a deregistered user i can ONLY register
    
    if (current_state == 1): #1 = register
        next_state = random.choice(register, p = p_register)

    elif (current_state==2) :#2 = uplink service 1
        next_state = random.choice(uplink_service1, p=p_uplink_service1) 

    elif (current_state == 3) :#3 = uplink service 2
        next_state = random.choice(uplink_service2, p = p_uplink_service2) 

    elif (current_state == 4) :#4 = uplink_service1_with_network_issues
        next_state = random.choice(uplink_service1_with_network_issues, p = p_uplink_service1_with_network_issues) 

    elif (current_state == 5) :#5 = uplink_service2_with_network_issues
        next_state = random.choice(uplink_service2_with_network_issues, p = p_uplink_service2_with_network_issues) 

    elif (current_state == 6) :#6 = uplink_service2_with_network_issues
        next_state = random.choice(downlink, p = p_downlink) 

    elif (current_state == 7) :#7 = uplink_service2_with_network_issues
        next_state = random.choice(pdu_s_release, p = p_pdu_s_release) 

    elif (current_state == 8) :#8 = uplink_service2_with_network_issues
        next_state = random.choice(idle, p = p_idle)

    else: #deregister (9) or initial state (0)
        next_state = 1 #can only register

    return next_state    
