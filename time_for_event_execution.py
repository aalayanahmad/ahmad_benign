from constants import PROCESSING_TIME_PER_EVENT, SERVICE_TIME, INTERVAL_TIME
import math
from numpy import random

def time_execution_current_event(current_event):
  
  if current_event == 1:
   return PROCESSING_TIME_PER_EVENT["register"]
 
  elif current_event == 2:
   return PROCESSING_TIME_PER_EVENT["uplink_any"]
  
  elif current_event == 3:
   return PROCESSING_TIME_PER_EVENT["uplink_service1"]
  
  elif current_event == 4:
   return PROCESSING_TIME_PER_EVENT["uplink_service2"]
  
  elif current_event == 5:
   return PROCESSING_TIME_PER_EVENT["uplink_service1_with_network_issues"]
  
  elif current_event == 6:
   return PROCESSING_TIME_PER_EVENT["uplink_servicew_with_network_issues"]
  
  elif current_event == 7:
   return PROCESSING_TIME_PER_EVENT["downlink"]
  
  elif current_event == 8:
   return PROCESSING_TIME_PER_EVENT["pdu_ue_release"]
  
  elif current_event == 9:
   return PROCESSING_TIME_PER_EVENT["pdu_gnb_release"]
  
  elif current_event == 10:
   return PROCESSING_TIME_PER_EVENT["idle"]
  
  else: 
   return PROCESSING_TIME_PER_EVENT["deregister"]

                             ############################################

def service_time():
 while True:
  x = -(SERVICE_TIME) * math.log(random.rand()) #10---------------3 for test with 5 minute long--------------------- ASK
  if x >= 2 and x <= INTERVAL_TIME: #x>8 #ASK
    break
 return x