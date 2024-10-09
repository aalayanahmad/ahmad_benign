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
    "uplink_banking"             : 7,
    "uplink_text"                : 7,
    "uplink_video"               : 7, 
    "downlink"                   : 7, 
    "ue_release"                 : 10, 
    "gnb_release"                : 2, 
    "deregister"                 : 3, 
    }


LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_SLICE1 = { 
    "register"         : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "uplink_google"    : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"],
    "uplink_banking"   : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"],
    "uplink_text"      : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"],
    "downlink"         : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "ue_release"       : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "gnb_release"      : ["uplink_google", "uplink_text", "uplink_banking"], 
    "deregister"       : ["register"]  
}

BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_SLICE1 = { 
    "register"         : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_google"    : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_banking"   : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_text"      : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "downlink"         : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "ue_release"       : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "gnb_release"      : [0.33, 0.33, 0.34],
    "deregister"       : [1]
}

LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_SLICE2 = { 
    "register"         : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "uplink_google"    : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"],
    "uplink_video"     : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"],
    "downlink"         : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "ue_release"       : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "gnb_release"      : ["uplink_google", "uplink_video"], 
    "deregister"       : ["register"]  
}

BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_SLICE2 = { 
    "register"         : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "uplink_google"    : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "uplink_video"     : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "downlink"         : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "ue_release"       : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "gnb_release"      : [0.5, 0.5],
    "deregister"       : [1]
}

LIST_OF_LAMBDAS = [1,3,5,8,6,2,1] 