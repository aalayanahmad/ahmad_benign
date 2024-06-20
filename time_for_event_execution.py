from constants import PROCESSING_TIME_PER_EVENT

def time_execution_current_event(current_event):
  if current_event==1:#ISS
   return PROCESSING_TIME_PER_EVENT["iss"]
  elif current_event==2:#registration
   return PROCESSING_TIME_PER_EVENT["register"]
  elif current_event==3:#uplink
   return PROCESSING_TIME_PER_EVENT["uplink"]
  elif current_event==4:#downlink
   return PROCESSING_TIME_PER_EVENT["downlink"]
  elif current_event==5:#pdu session
   return PROCESSING_TIME_PER_EVENT["PDU_sRelease"]
  elif current_event==6:#idle
   return PROCESSING_TIME_PER_EVENT["idle"]
  else: #deregistration 
   return PROCESSING_TIME_PER_EVENT["deregister"]
