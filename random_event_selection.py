from numpy import random

def random_event_selection(current_state, register, uplink_any, uplink_service1, uplink_service2, 
                           uplink_service1_delayed, uplink_service2_delayed, 
                           downlink, pdu_ue_release, pdu_gnb_release, idle, probability_register, probability_uplink_any, 
                           probability_uplink_service1, probability_uplink_service2, 
                           probability_uplink_service1_delayed, probability_uplink_service2_delayed, probability_downlink, 
                           probability_pdu_ue_release, probability_pdu_gnb_release, probability_idle):
    
    
    if (current_state == 1): 
        next_state = random.choice(register, p = probability_register)
    
    elif (current_state == 2) :
        next_state = random.choice(uplink_any, p = probability_uplink_any) 
    
    elif (current_state == 3) :
        next_state = random.choice(uplink_service1, p = probability_uplink_service1) 

    elif (current_state == 4) :
        next_state = random.choice(uplink_service2, p = probability_uplink_service2) 

    elif (current_state == 5) :
        next_state = random.choice(uplink_service1_delayed, p = probability_uplink_service1_delayed) 

    elif (current_state == 6) :
        next_state = random.choice(uplink_service2_delayed, p = probability_uplink_service2_delayed) 

    elif (current_state == 7) :
        next_state = random.choice(downlink, p = probability_downlink) 

    elif (current_state == 8) :
        next_state = random.choice(pdu_ue_release, p = probability_pdu_ue_release) 

    elif (current_state == 9) :
        next_state = random.choice(pdu_gnb_release, p = probability_pdu_gnb_release) 

    elif (current_state == 10) :
        next_state = random.choice(idle, p = probability_idle)

    else: #deregister
        next_state = 1 

    return next_state    
