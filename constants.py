NUMBER_OF_UES_PER_SLICE = 150 #i have two slices so 150 per slice is enough
INTERVAL_TIME = 15.0 #(minutes)
SERVICE_TIME = 12 #the maximum amount of time a UE can spend in the network per time slot!    
EVENTS_PER_MINUTE = 15 #how many events can happen per minute (per ue or across ues?)
PROCESSING_TIME_PER_EVENT = { "register": 10, "uplink": 2, "downlink": 2, "PDU_sRelease": 5, "idle": 0, "deregister": 2 }