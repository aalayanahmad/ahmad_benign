NUMBER_OF_UES_PER_SLICE = 50

INTERVAL_TIME = 13.0 

MEAN_SERVICE_TIME = 12 # the average amount of time a UE can spend in the network during each time slot

EVENTS_PER_SECOND = 0.1 #so 6 per minute, how many events can happen per second per ue

PROCESSING_TIME_PER_EVENT = { #event: time to process the event
    1 : 10, #REGISTER 
    2 : 3, #UPLINK
    3 : 3, #DOWNLINK
    4 : 7, #PDU_UE_RELEASE
    5 : 7, #PDU_GNB_RELEASE
    6 : 4, #DEREGISTER
    }

LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT = { 
    1 : [2, 3, 4, 5], #REGISTER
    2 : [3, 4, 5], #UPLINK
    3 : [2, 4, 5], #DOWNLINK
    4 : [2, 3, 5], #PDU_UE_RELEASE
    5 : [2, 3], #PDU_GNB_RELEASE
    6 : [1]  #DEREGISTER
}

#BENIGN PROBABILITIES
#in a bengin scenario everything is equally probable!
PRBABILITIES_OF_LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_BENIGN = { 
    1 : [0.25, 0.25, 0.25, 0.25], #REGISTER
    2 : [0.33, 0.33, 0.34], #UPLINK
    3 : [0.33, 0.33, 0.34], #DOWNLINK
    4 : [0.33, 0.33, 0.34], #PDU_UE_RELEASE
    5 : [0.5, 0.5], #PDU_GNB_RELEASE
    6 : [1] #DEREGISTER
}

LIST_OF_LAMBDAS = [1,3,5,7,5,3,1]