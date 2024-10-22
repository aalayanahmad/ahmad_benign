NUMBER_OF_UES_PER_SLICE = 56

INTERVAL_TIME = 7.0 

#the average amount of time a UE can spend in the network during each time slot
MEAN_SERVICE_TIME = 50

#how many events can happen per second per ue
EVENTS_PER_MINUTE = 9

#time it takes for each procedure to complete (with some buffer time)
PROCESSING_TIME_PER_EVENT = {
    "register"                   : 13, 
    "uplink_google"              : 7, 
    "uplink_banking"             : 5, #it takes 3 seconds but give 2 seconds guard time similarly for the others!
    "uplink_text"                : 5,
    "uplink_video"               : 5, 
    "uplink_banking_unstable"    : 5, #it takes 3 seconds but give 2 seconds guard time similarly for the others!
    "uplink_text_unstable"       : 5,
    "uplink_video_unstable"      : 5, 
    "uplink_banking_attack"      : 5, #it takes 3 seconds but give 2 seconds guard time similarly for the others!
    "uplink_text_attack"         : 5,
    "downlink"                   : 7, 
    "ue_release"                 : 13, 
    "gnb_release"                : 5, 
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
    "register"                  : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"], 
    "uplink_google"             : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"],
    "uplink_video"              : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"],
    "uplink_video_unstable"     : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"],
    "downlink"                  : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"], 
    "ue_release"                : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"], 
    "gnb_release"               : ["uplink_google", "uplink_video", "uplink_video_unstable"], 
    "deregister"                : ["register"]  
}

BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_UNSTABLE_SLICE2 = { 
    "register"         : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_google"    : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_video"     : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2],  
    "downlink"         : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "ue_release"       : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "gnb_release"      : [0.33, 0.33, 0.34],
    "deregister"       : [1]
}

##ATTACKISH##
LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_ATTACKISH_SLICE1 = { 
    "register"         : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "uplink_google"    : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"],
    "uplink_banking"   : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"],
    "uplink_text"      : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"],
    "downlink"         : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "ue_release"       : ["uplink_google", "uplink_text", "uplink_banking", "downlink", "ue_release", "gnb_release"], 
    "gnb_release"      : ["uplink_google", "uplink_text", "uplink_banking"], 
    "deregister"       : ["register"]  
}

BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_ATTACKISH_SLICE1 = { 
    "register"         : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_google"    : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_banking"   : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "uplink_text"      : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "downlink"         : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "ue_release"       : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
    "gnb_release"      : [0.33, 0.33, 0.34],
    "deregister"       : [1]
}
##same as unstable can also be stable we dont have attack here
# LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_ATTACKISH_SLICE2 = { 
#     "register"                  : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"], 
#     "uplink_google"             : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"],
#     "uplink_video"              : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"],
#     "uplink_video_unstable"     : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"],
#     "downlink"                  : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"], 
#     "ue_release"                : ["uplink_google", "uplink_video", "uplink_video_unstable", "downlink", "ue_release", "gnb_release"], 
#     "gnb_release"               : ["uplink_google", "uplink_video", "uplink_video_unstable"], 
#     "deregister"                : ["register"]  
# }

# BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_ATTACKISH_SLICE2 = { 
#     "register"         : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
#     "uplink_google"    : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
#     "uplink_video"     : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2],  
#     "downlink"         : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
#     "ue_release"       : [0.16, 0.16, 0.16, 0.16, 0.16, 0.2], 
#     "gnb_release"      : [0.33, 0.33, 0.34],
#     "deregister"       : [1]
# }

LIST_OF_LAMBDAS = [1,3,5,8,6,2,1] 