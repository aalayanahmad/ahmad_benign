NUMBER_OF_UES_PER_SLICE = 40

INTERVAL_TIME = 10.0 

SERVICE_TIME = 12 # the maximum amount of time a UE can spend in the network during each time slot

EVENTS_PER_MINUTE = 18 # how many events can happen per minute (per ue or across ues?) ASK

PROCESSING_TIME_PER_EVENT = { #event: time to process the event
    1 : 60, 
    2 : 20, 
    3 : 35, 
    4 : 35,
    5 : 35,
    6 : 35, 
    7 : 20, 
    8 : 60, 
    9 : 60, 
    10: 60 
    }

LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT = { 
    1 : [2, 3, 4, 5, 6, 7, 8, 9], #REGISTER
    2 : [3, 4, 5, 6, 7, 8, 9], #UPLINK_ANY
    3 : [2, 4, 5, 6, 7, 8, 9], #UPLINK_SERVICE1 
    4:  [2, 3, 5, 6, 7, 8, 9], #UPLINK_SERVICE2
    5 : [2, 3, 4, 6, 7, 8, 9], #UPLINK_SERVICE1_DELAYED
    6 : [2, 3, 4, 5, 7, 8, 9], #UPLINK_SERVICE2_DELAYED
    7 : [2, 3, 4, 5, 6, 8, 9], #DOWNLINK
    8 : [2, 3, 4, 5, 6, 7, 9], #PDU_UE_RELEASE
    9 : [2, 3, 4, 5, 6, 7], #PDU_GNB_RELEASE
    10 : [1]  #DEREGISTER
}

#BENIGN PROBABILITIES
#in a bengin scenario everything is equally probable!
PRBABILITIES_OF_LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_BENIGN = { 
    1 : [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], #REGISTER
    2 : [0.14, 0.14, 0.14, 0.14 , 0.14 , 0.14, 0.16], #UPLINK_ANY
    3 : [0.14, 0.14, 0.14, 0.14 , 0.14 , 0.14, 0.16], #UPLINK_SERVICE1 
    4:  [0.14, 0.14, 0.14, 0.14 , 0.14 , 0.14, 0.16], #UPLINK_SERVICE2
    5 : [0.14, 0.14, 0.14, 0.14 , 0.14 , 0.14, 0.16], #UPLINK_SERVICE1_DELAYED
    6 : [0.14, 0.14, 0.14, 0.14 , 0.14 , 0.14, 0.16], #UPLINK_SERVICE2_DELAYED
    7 : [0.14, 0.14, 0.14, 0.14 , 0.14 , 0.14, 0.16], #DOWNLINK
    8 : [0.14, 0.14, 0.14, 0.14 , 0.14 , 0.14, 0.16], #PDU_UE_RELEASE
    9 : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], #PDU_GNB_RELEASE
    10 : [1] #DEREGISTER
}

LIST_OF_LAMBDAS = [1,3,5,7,5,3,1]