from ahmad_benign.constants_RN import PROCESSING_TIME_PER_EVENT, MEAN_SERVICE_TIME, INTERVAL_TIME
import math
from numpy import random

def time_execution_current_event(current_event):
   return PROCESSING_TIME_PER_EVENT[current_event]

                             ############################################

def service_time():
   while True:
      x = -(MEAN_SERVICE_TIME) * math.log(random.random())
      if (x >= 0 and x <= INTERVAL_TIME): 
         break
   return x