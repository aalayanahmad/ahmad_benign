NUMBER_OF_UES_PER_SLICE = 150 # i have two slices, and i want 150 ues per slice

INTERVAL_TIME = 15.0 # in minutes

SERVICE_TIME = 15 # the maximum amount of time a UE can spend in the network per time slot

EVENTS_PER_MINUTE = 15 # how many events can happen per minute (per ue or across ues?) ASK

PROCESSING_TIME_PER_EVENT = { 
                             "register": 10, "uplink_any": 2, 
                             "uplink_service1": 15, "uplink_service2": 15,
                             "uplink_service1_delayed": 15, "uplink_service2_delayed": 15, 
                             "downlink": 2, "pdu_ue_release": 5, "pdu_gnb_release": 5, "idle": 0, "deregister": 2 
                             }


REGISTER = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] #1
UPLINK_ANY = [3, 4, 5, 6, 7, 8, 9, 10, 11] #2 
UPLINK_SERVICE1 = [2, 4, 5, 6, 7, 8, 9, 10, 11] #3 
UPLINK_SERVICE2 = [2, 3, 5, 6, 7, 8, 9, 10, 11] #4
UPLINK_SERVICE1_DELAYED = [2, 3, 4, 6, 7, 8, 9, 10, 11] #5
UPLINK_SERVICE2_DELAYED = [2, 3, 4, 5, 7, 8, 9, 10, 11] #6
DOWNLINK = [2, 3, 4, 5, 6, 8, 9, 10, 11] #7
PDU_UE_RELEASE = [2, 3, 4, 5, 6, 7, 9, 10, 11] #8
PDU_GNB_RELEASE = [2, 3, 4, 5, 6, 7, 8, 10, 11] #9
IDLE = [2, 3, 4, 5, 6, 7] #10   #NOT SO SURE ASK
DEREGISTER = [1] #11 


#BENIGN PROBABILITIES
#in a bengin scenario everything is equally probable!
PB_REGISTER = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1] #1
PB_UPLINK_ANY = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #2 
PB_UPLINK_SERVICE1 = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #3 
PB_UPLINK_SERVICE2 = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #4
PB_UPLINK_SERVICE1_DELAYED = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #5
PB_UPLINK_SERVICE2_DELAYED = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #6
PB_DOWNLINK = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #7
PB_PDU_UE_RELEASE = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #8
PB_PDU_GNB_RELEASE = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #9
PB_IDLE = [0.16, 0.16, 0.16, 0.16, 0.16, 0.2] #10
PB_DEREGISTER = [1] #11 

LIST_OF_LAMBDAS = [1,3,5,7,8,6,4,2] #ASK