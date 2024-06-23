from constants import PROCESSING_TIME_PER_EVENT, SERVICE_TIME, INTERVAL_TIME
import math
from numpy import random

def time_execution_current_event(current_event):
   return PROCESSING_TIME_PER_EVENT[current_event]

                             ############################################

def service_time():
 while True:
  x = -(SERVICE_TIME) * math.log(random.rand()) #ASK
  if (x >= 2 and x <= INTERVAL_TIME): 
    break
 return x