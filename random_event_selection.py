from numpy import random

def random_event_selection(current_state, register, uplink_any, uplink_service1, uplink_service2, 
                           uplink_service1_with_network_issues, uplink_service2_with_network_issues, 
                           downlink, pdu_ue_release, pdu_gnb_release, idle, p_register, p_uplink_any, p_uplink_service1, p_uplink_service2, 
                           p_uplink_service1_with_network_issues, p_uplink_service2_with_network_issues, p_downlink, 
                           p_pdu_ue_release, p_pdu_gnb_release, p_idle):
    
    
    if (current_state == 1): 
        next_state = random.choice(register, p = p_register)
    elif (current_state==2) :
        next_state = random.choice(uplink_any, p = p_uplink_any) 
    elif (current_state==3) :
        next_state = random.choice(uplink_service1, p = p_uplink_service1) 

    elif (current_state == 4) :
        next_state = random.choice(uplink_service2, p = p_uplink_service2) 

    elif (current_state == 5) :
        next_state = random.choice(uplink_service1_with_network_issues, p = p_uplink_service1_with_network_issues) 

    elif (current_state == 6) :
        next_state = random.choice(uplink_service2_with_network_issues, p = p_uplink_service2_with_network_issues) 

    elif (current_state == 7) :
        next_state = random.choice(downlink, p = p_downlink) 

    elif (current_state == 8) :
        next_state = random.choice(pdu_ue_release, p = p_pdu_ue_release) 

    elif (current_state == 9) :
        next_state = random.choice(pdu_gnb_release, p = p_pdu_gnb_release) 

    elif (current_state == 10) :
        next_state = random.choice(idle, p = p_idle)

    else: 
        next_state = 1 

    return next_state    
