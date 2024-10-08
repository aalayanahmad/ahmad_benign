NUMBER_OF_UES_PER_SLICE = 45

INTERVAL_TIME = 5.0 

#the average amount of time a UE can spend in the network during each time slot
MEAN_SERVICE_TIME = 35

#how many events can happen per second per ue
EVENTS_PER_MINUTE = 8

#time it takes for each procedure to complete (with some buffer time)
PROCESSING_TIME_PER_EVENT = {
    "register"                   : 8, 
    "uplink_google"              : 7, 
    "uplink_text"                : 7,
    "uplink_video"               : 7,
    "uplink_banking"             : 7, 
    "downlink"                   : 7, 
    "ue_release"                 : 10, 
    "gnb_release"                : 2, 
    "deregister"                 : 3, 
    }

#the legal events to move to from each event
LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT = { 
    "register"    : ["uplink_google", "uplink_text", "uplink_video", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "uplink"      : ["uplink_google", "uplink_text", "uplink_video", "uplink_banking", "downlink", "ue_release", "gnb_release"],
    "downlink"    : ["uplink_google", "uplink_text", "uplink_video", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "ue_release"  : ["uplink_google", "uplink_text", "uplink_video", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "gnb_release" : ["uplink_google", "uplink_text", "uplink_video", "uplink_banking"], 
    "deregister"  : ["register"]  
}

#a truthful ue will not bias an event over other, therefore everything is equally probable in the benign case
BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS = { 
    "register"    : [0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.16], 
    "uplink"      : [0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.16], 
    "downlink"    : [0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.16], 
    "ue_release"  : [0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.16], 
    "gnb_release" : [0.25, 0.25, 0.25, 0.25],
    "deregister"  : [1]
}

LIST_OF_LAMBDAS = [1,3,5,8,6,2,1] 