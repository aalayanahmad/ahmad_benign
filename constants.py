NUMBER_OF_UES_PER_SLICE = 150 

INTERVAL_TIME = 900.0 # in seconds => 15 minutes

SERVICE_TIME = 20 # the maximum amount of time a UE can spend in the network per time slot in 

EVENTS_PER_MINUTE = 15 # how many events can happen per minute (per ue or across ues?) ASK

PROCESSING_TIME_PER_EVENT = { 
    1 : 10, #register: time to process a register event, similarly for the rest
    2 : 2, 
    3 : 15, 
    4 : 15,
    5 : 15,
    6 : 15, 
    7 : 2, 
    8 : 5, 
    9 : 5, 
    10: 0, 
    11: 2 
    }

LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT = { 
    1 : [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], #REGISTER
    2 : [3, 4, 5, 6, 7, 8, 9, 10, 11], #UPLINK_ANY
    3 : [2, 4, 5, 6, 7, 8, 9, 10, 11], #UPLINK_SERVICE1 
    4: [2, 3, 5, 6, 7, 8, 9, 10, 11], #UPLINK_SERVICE2
    5 : [2, 3, 4, 6, 7, 8, 9, 10, 11], #UPLINK_SERVICE1_DELAYED
    6 : [2, 3, 4, 5, 7, 8, 9, 10, 11], #UPLINK_SERVICE2_DELAYED
    7 : [2, 3, 4, 5, 6, 8, 9, 10, 11], #DOWNLINK
    8 : [2, 3, 4, 5, 6, 7, 9, 10, 11], #PDU_UE_RELEASE
    9 : [2, 3, 4, 5, 6, 7, 8, 10, 11], #PDU_GNB_RELEASE
    10 : [2, 3, 4, 5, 6, 7], #10  #IDLE #NOT SO SURE ASK
    11 : [1] #11  #DEREGISTER
}

#BENIGN PROBABILITIES
#in a bengin scenario everything is equally probable!
PRBABILITIES_OF_LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_BENIGN = { 
    1 : [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], #REGISTER
    2 : [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12], #UPLINK_ANY
    3 : [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12], #UPLINK_SERVICE1 
    4: [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12], #UPLINK_SERVICE2
    5 : [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12], #UPLINK_SERVICE1_DELAYED
    6 : [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12], #UPLINK_SERVICE2_DELAYED
    7 : [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12], #DOWNLINK
    8 : [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12], #PDU_UE_RELEASE
    9 : [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12], #PDU_GNB_RELEASE
    10 : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], #10  #IDLE #NOT SO SURE ASK
    11 : [1] #11  #DEREGISTER
}

LIST_OF_LAMBDAS = [1,3,5,7,8,6,4,2]