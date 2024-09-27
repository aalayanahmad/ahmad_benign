from constants import PROCESSING_TIME_PER_EVENT, MEAN_SERVICE_TIME, INTERVAL_TIME
import math
from numpy import random

def time_execution_current_event(current_event):
   return PROCESSING_TIME_PER_EVENT[current_event]

                             ############################################

def service_time():
   random_seed = random.randint(0, 10000)  
   random.seed(random_seed)
   while True:
      x = -(MEAN_SERVICE_TIME) * math.log(random.random())
      if (x >= 3 and x <= INTERVAL_TIME): 
         break
   return x