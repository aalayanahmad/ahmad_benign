NUMBER_OF_UES_PER_SLICE = 56

INTERVAL_TIME = 10.0 

#the average amount of time a UE can spend in the network during each time slot
MEAN_SERVICE_TIME = 40

#how many events can happen per second per ue
EVENTS_PER_MINUTE = 12

#time it takes for each procedure to complete (with some buffer time)
PROCESSING_TIME_PER_EVENT = {
    "register"                   : 5, 
    "uplink_google"              : 6, 
    "uplink_banking"             : 4, 
    "uplink_text"                : 4,
    "uplink_video"               : 4, 
    "uplink_banking_unstable"    : 4, 
    "uplink_text_unstable"       : 4,
    "uplink_video_unstable"      : 4, 
    "uplink_banking_attack"      : 4, 
    "uplink_text_attack"         : 4,
    "downlink"                   : 2, 
    "ue_release"                 : 4, 
    "gnb_release"                : 2, 
    "deregister"                 : 3, 
    }
##NO ACTUAL ATTACK ON 2!


##STABLE NETWORK##
LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_STABLE_SLICE1 = { 
    "register"         : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "uplink_google"    : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"],
    "uplink_banking"   : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"],
    "uplink_text"      : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"],
    "downlink"         : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "ue_release"       : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "gnb_release"      : ["uplink_google", "uplink_text", "uplink_banking"], 
    "deregister"       : ["register"]  
}

BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_STABLE_SLICE1 = { 
    "register"         : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_google"    : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_banking"   : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_text"      : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "downlink"         : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "ue_release"       : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "gnb_release"      : [0.33, 0.33, 0.34],
    "deregister"       : [1]
}

LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_STABLE_SLICE2 = { 
    "register"         : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "uplink_google"    : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"],
    "uplink_video"     : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"],
    "downlink"         : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "ue_release"       : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "gnb_release"      : ["uplink_google", "uplink_video"], 
    "deregister"       : ["register"]  
}

BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_STABLE_SLICE2 = { 
    "register"         : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "uplink_google"    : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "uplink_video"     : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "downlink"         : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "ue_release"       : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "gnb_release"      : [0.5, 0.5],
    "deregister"       : [1]
}

##UNSTABLE NETWORK##
LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_UNSTABLE_SLICE1 = { 
    "register"                  : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"], 
    "uplink_google"             : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"],
    "uplink_banking"            : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"],
    "uplink_text"               : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"],
    "uplink_banking_unstable"   : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"],
    "uplink_text_unstable"      : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"],
    "downlink"                  : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"], 
    "ue_release"                : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"], 
    "gnb_release"               : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable"], 
    "deregister"                : ["register"]  
}

BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_UNSTABLE_SLICE1 = {
    "register"                 : [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], 
    "uplink_google"            : [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], 
    "uplink_banking"           : [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], 
    "uplink_text"              : [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], 
    "uplink_banking_unstable"  : [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], 
    "uplink_text_unstable"     : [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], 
    "downlink"                 : [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], 
    "ue_release"               :  [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], 
    "gnb_release"              : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "deregister"               : [1]
}

LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_UNSTABLE_SLICE2 = { 
    "register"         : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "uplink_google"    : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"],
    "uplink_video"     : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"],
    "downlink"         : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "ue_release"       : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "gnb_release"      : ["uplink_google", "uplink_video"], 
    "deregister"       : ["register"]  
}

BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_UNSTABLE_SLICE2 = { 
    "register"         : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "uplink_google"    : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "uplink_video"     : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "downlink"         : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "ue_release"       : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "gnb_release"      : [0.5, 0.5],
    "deregister"       : [1]
}

##ATTACKISH##
LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_ATTACKISH_SLICE1 = { 
    "register"                  : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"], 
    "uplink_google"             : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"],
    "uplink_banking"            : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"],
    "uplink_text"               : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"],
    "uplink_banking_unstable"   : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"],
    "uplink_text_unstable"      : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"],
    "downlink"                  : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"], 
    "ue_release"                : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable", "downlink", "ue_release", "gnb_release"], 
    "gnb_release"               : ["uplink_google", "uplink_text", "uplink_banking",  "uplink_text_unstable", "uplink_banking_unstable"], 
    "deregister"                : ["register"]  
}

BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_ATTACKISH_SLICE1 = {
    "register"                 : [0.04, 0.04, 0.04, 0.26, 0.26, 0.04, 0.28, 0.04], 
    "uplink_google"            :  [0.04, 0.04, 0.04, 0.26, 0.26, 0.04, 0.28, 0.04], 
    "uplink_banking"           :  [0.04, 0.04, 0.04, 0.26, 0.26, 0.04, 0.28, 0.04],  
    "uplink_text"              :  [0.04, 0.04, 0.04, 0.26, 0.26, 0.04, 0.28, 0.04], 
    "uplink_banking_unstable"  : [0.04, 0.04, 0.04, 0.26, 0.26, 0.04, 0.28, 0.04],  
    "uplink_text_unstable"     :  [0.04, 0.04, 0.04, 0.26, 0.26, 0.04, 0.28, 0.04], 
    "downlink"                 :  [0.04, 0.04, 0.04, 0.26, 0.26, 0.04, 0.28, 0.04], 
    "ue_release"               :  [0.04, 0.04, 0.04, 0.26, 0.26, 0.04, 0.28, 0.04], 
    "gnb_release"              : [0.08, 0.06, 0.06, 0.4, 0.4], 
    "deregister"               : [1]
}

LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_ATTACKISH_SLICE2 = { 
    "register"         : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "uplink_google"    : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"],
    "uplink_video"     : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"],
    "downlink"         : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "ue_release"       : ["uplink_google", "uplink_video", "downlink", "ue_release", "gnb_release"], 
    "gnb_release"      : ["uplink_google", "uplink_video"], 
    "deregister"       : ["register"]  
}

BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_ATTACKISH_SLICE2 = { 
    "register"         : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "uplink_google"    : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "uplink_video"     : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "downlink"         : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "ue_release"       : [0.2, 0.2, 0.2, 0.2, 0.2], 
    "gnb_release"      : [0.5, 0.5],
    "deregister"       : [1]
}

LIST_OF_LAMBDAS = [2,5,8,10,11,6,3,2] 