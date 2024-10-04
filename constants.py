NUMBER_OF_UES_PER_SLICE = 5

INTERVAL_TIME = 3.0 

#the average amount of time a UE can spend in the network during each time slot
MEAN_SERVICE_TIME = 7 

#how many events can happen per second per ue
EVENTS_PER_MINUTE = 5 

#time it takes for each procedure to complete (with some buffer time)
PROCESSING_TIME_PER_EVENT = {
    "register"    : 10, 
    "uplink"      : 5, 
    "downlink"    : 5, 
    "ue_release"  : 6, 
    "gnb_release" : 2, 
    "deregister"  : 4, 
    }

#the legal events to move to from each event
LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT = { 
    "register"    : ["uplink", "downlink", "ue_release", "gnb_release"], 
    "uplink"      : ["uplink", "downlink", "ue_release", "gnb_release"],
    "downlink"    : ["uplink", "downlink", "ue_release", "gnb_release"], 
    "ue_release"  : ["uplink", "downlink", "ue_release", "gnb_release"], 
    "gnb_release" : ["uplink"], 
    "deregister"  : ["register"]  
}

#a truthful ue will not bias an event over other, therefore everything is equally probable in the benign case
BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS = { 
    "register"    : [0.25, 0.25, 0.25, 0.25], 
    "uplink"      : [0.25, 0.25, 0.25, 0.25], 
    "downlink"    : [0.25, 0.25, 0.25, 0.25], 
    "ue_release"  : [0.25, 0.25, 0.25, 0.25], 
    "gnb_release" : [1],
    "deregister"  : [1]
}

LIST_OF_LAMBDAS = [1,2,3,4] 