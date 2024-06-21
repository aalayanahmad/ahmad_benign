NUMBER_OF_UES_PER_SLICE = 150 #i have two slices so 150 per slice is enough
INTERVAL_TIME = 15.0 #(minutes)
SERVICE_TIME = 12 #the maximum amount of time a UE can spend in the network per time slot!    
EVENTS_PER_MINUTE = 15 #how many events can happen per minute (per ue or across ues?)
PROCESSING_TIME_PER_EVENT = { 
                             "register": 10, "uplink_any": 2, 
                             "uplink_service1": 15, "uplink_service2": 15,
                             "uplink_service1_with_network_issues": 15, "uplink_service2_with_network_issues": 15, 
                             "downlink": 2, "pdu_ue_release": 5, "pdu_gnb_release": 5, "idle": 0, "deregister": 2 
                             }