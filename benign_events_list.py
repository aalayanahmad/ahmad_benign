from file_handling import *
from constants import NUMBER_OF_UES_PER_SLICE, INTERVAL_TIME, SERVICE_TIME
from numpy import random
import math
from time_for_event_execution import *
from list_event import *

def benign_events_list():
    
    #at each state x i can go to any of the other states in x's corresponding array 
    register = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] #1
    uplink_any = [3, 4, 5, 6, 7, 8, 9, 10, 11] #2 
    uplink_service1 = [2, 4, 5, 6, 7, 8, 9, 10, 11] #3 
    uplink_service2 = [2, 3, 5, 6, 7, 8, 9, 10, 11] #4
    uplink_service1_with_network_issues = [2, 3, 4, 6, 7, 8, 9, 10, 11] #5
    uplink_service2_with_network_issues = [2, 3, 4, 5, 7, 8, 9, 10, 11] #6
    downlink = [2, 3, 4, 5, 6, 8, 9, 10, 11] #7
    pdu_ue_release = [2, 3, 4, 5, 6, 7, 9, 10, 11] #8
    pdu_gnb_release = [2, 3, 4, 5, 6, 7, 8, 10, 11] #9
    idle = [2, 3, 4, 5, 6, 7] #10   #NOT SO SURE ASK
    deregister = [1] #11 

    #in a bengin scenario everything is equally probable!
    probability_register = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1] #1
    probability_uplink_any = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #2 
    probability_uplink_service1 = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #3 
    probability_uplink_service2 = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #4
    probability_uplink_service1_with_network_issues = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #5
    probability_uplink_service2_with_network_issues = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #6
    probability_downlink = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #7
    probability_pdu_ue_release = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #8
    probability_pdu_gnb_release = [0.11, 0.11, 0.11, 0.11 , 0.11 , 0.11, 0.11, 0.11, 0.12] #9
    probability_idle = [0.16, 0.16, 0.16, 0.16, 0.16, 0.2] #10
    probability_deregister = [1] #11 
    
    #deleteonefile('/home/ubuntu/UERANSIM/script/files/normal_scenario_event.txt')
    #deletefiles('/home/ubuntu/UERANSIM/config/') ASK

    # creating_ue_file_names(NUMBER_OF_UES_PER_SLICE,1,2,1)# creating yaml files #ASK
    # creating_ue_file_names(NUMBER_OF_UES_PER_SLICE,2,3,2)

    #ASK WHY NOT ONE TIME USAGE?
    yamlfiles(NUMBER_OF_UES_PER_SLICE, 1, 3, 1) #create UEs of slice 1 and 2
    
    ue_state = dict() #to manage the different ue states throughout the program
    ues_list = [] #to create the ue pool 
    ue_selected = [] #to control the number of ues that has been selected.
    list_to_execute = []
    temp_ue_list = []
    
    list_of_lambdas = [1,3,5,7,8,6,4,2] #ASK
    slot_time=0.0

    for lambda_value in list_of_lambdas:
      number_of_ues_for_this_lambda = lambda_value * INTERVAL_TIME
      counter = 1
      if (lambda_value > 1):
        temp_ue_list = [ue_temp for ue_temp in ue_selected if ue_state[ue_temp + "_D"] >= slot_time] #deregister? ASK
        ue_selected.clear()
        ueselected = temp_ue_list.copy()
        ues_list = ues_list(0, NUMBER_OF_UES_PER_SLICE) #cause we need all of them
        while counter <= number_of_ues_for_this_lambda:
          selected_ue = random.choice(ues_list)
          if selected_ue in ue_selected: #checking that ues are not repeated
            continue
          else: 
            ue_selected.append(selected_ue)
            ue_state[selected_ue + "_A"] = - (1/lambda_value) * math.log(random.rand()) + slot_time 
            ue_state[selected_ue + "_D"] = ue_state[selected_ue + "_A"] + service_time()    
            
            list_event(selected_ue, ue_state[selected_ue + "_A"], ue_state[selected_ue + "_D"],
                       register, uplink_any, uplink_service1, uplink_service2, uplink_service1_with_network_issues, 
                       uplink_service2_with_network_issues, downlink, pdu_ue_release, pdu_gnb_release, idle, 
                       probability_register, probability_uplink_any, probability_uplink_service1, probability_uplink_service2,
                       probability_uplink_service1_with_network_issues, probability_uplink_service2_with_network_issues, 
                       probability_downlink, probability_pdu_ue_release, probability_pdu_gnb_release, probability_idle,
                       list_to_execute,lambda_value, counter) #sending the ue's state, and configuration accordingly to first scenarios(it is done for the 3 attack and normal behavior)
            counter+=1 #counting number of selected UEs
            slot_time += INTERVAL_TIME 

        list_to_execute.sort(key = takefourth)

        with open('/home/ubuntu/UERANSIM/script/files/BeningList_attack1.txt', 'w') as file:
          for line in list_to_execute:
            file.write(','.join(str(item) for item in line))
            file.write("\n" )

        for i in list_to_execute:
          print(i)
          
        return list_to_execute