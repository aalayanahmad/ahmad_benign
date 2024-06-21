from random_event_selection import *
from constants import EVENTS_PER_MINUTE
import math
from time_for_event_execution import *

def list_event(selected_ue, start, end,
              register, uplink_any, uplink_service1, uplink_service2, uplink_service1_with_network_issues, 
              uplink_service2_with_network_issues, downlink, pdu_ue_release, pdu_gnb_release, idle, 
              probability_register, probability_uplink_any, probability_uplink_service1, probability_uplink_service2,
              probability_uplink_service1_with_network_issues, probability_uplink_service2_with_network_issues, 
              probability_downlink, probability_pdu_ue_release, probability_pdu_gnb_release, probability_idle,
              arr, lamba_value, i):

    print(str(i) + ")" + selected_ue + " init: " + str(start) + "(" + str(start * 60) + ")" + 
          " end:" + str(end) + "(" + str(end*60) + ")" + " lda:" + str(lamba_value))
    
    end_to_seconds = end * 60 #pasing minutes to seconds
    #arr.append([selectedue,0,2,init*60,lambdaV,init,0]) #0=deregister,2=register
    arr.append([int(selected_ue[2:5]),2,start*60,lamba_value]) #0=deregister,2=register

    current_state = 2
    time = (start * 60) #time to control the while structure in seconds

    c = 0
    while (time <= (end_to_seconds - 10)): # (processtime["iss"]+5)
      event_to_trigger = random_event_selection(current_state, register, uplink_any, uplink_service1, uplink_service2, 
                           uplink_service1_with_network_issues, uplink_service2_with_network_issues, 
                           downlink, pdu_ue_release, pdu_gnb_release, idle, probability_register, probability_uplink_any, probability_uplink_service1, 
                           probability_uplink_service2, probability_uplink_service1_with_network_issues, probability_uplink_service2_with_network_issues, p_downlink, 
                           probability_downlink, probability_pdu_ue_release, probability_pdu_gnb_release, probability_idle)
      current_event = current_state
      #poisson=(-(1/(lambdaV+0.1))*math.log(random.rand()))*60 #------------------(-(1/(events_per_minute))*math.log(random.rand()))*60
      poisson = (-(1/(EVENTS_PER_MINUTE))*math.log(random.rand()))*60 #------------------(-(1/(events_per_minute))*math.log(random.rand()))*60
      if (math.floor(poisson) < time_execution_current_event(current_state)):
            p = time + time_execution_current_event(currentstate)
      else:
            p = time + poisson 
    if ((p)<=(end_to_seconds-10)): #(processtime["iss"]+5)
      time = p #(poisson+time_execution_current_event(current_event))---------------------
    #arr.append([selectedue,current_event,event_to_trigger,time,lambdaV,poisson,lambdaV+1])
      arr.append([int(selected_ue[2:5]),event_to_trigger,time,lamba_value])
      currentstate= event_to_trigger
    else:
      c+=1
    if c==3:
      break
      #arr.append([selectedue,currentstate,0,end*60,lambdaV,end,0])   
arr.append([int(selectedue[2:5]),0,end*60,lambdaV])

    return arr