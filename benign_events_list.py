from file_handling import *
from constants import NUMBER_OF_UES_PER_SLICE, INTERVAL_TIME, SERVICE_TIME
from numpy import random
import math
from time_for_event_execution import *

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
    yamlfiles(NUMBER_OF_UES_PER_SLICE, 1, 2, 1) #create UEs of slice 1
    yamlfiles(NUMBER_OF_UES_PER_SLICE, 2, 3, 2) #create UEs of slice 2
    
    ue_state = dict() #to manage the different ue states throughout the programm
    ues_list = [] #to create the ue pool 
    ue_selected = [] #to control the number of ues that has been selected.
    list_to_execute = []
    temp_ue_list = []
    to_DeleteueState = []
    
    list_of_lambdas= [1,3,5,7,8,6,4,2] #ASK #[2,4,6,8,10,8,6,4] #[10,25,35,20]#10,20,30,15#[2,4,5,7,9,7,6,4]-[2,4,6,8,10,8,6,4]#[1,2,3,4,5,4,3,2]
    slot_time=0.0

    for lambda_value in list_of_lambdas:
      ues_number_for_this_lambda = lambda_value * INTERVAL_TIME
      counter = 1
      if (lambda_value > 1):
        temp_ue_list = [ue_temp for ue_temp in ue_selected if ue_state[ue_temp + "_D"] >= slot_time] #deregister? ASK
        ue_selected.clear()
        ueselected = temp_ue_list.copy()
        print("ueselected list:")
        print(ueselected)
        print ("******************************************")
        print(ues_list)
        print ("******************************************")
        ues_list = ues_list(0, NUMBER_OF_UES_PER_SLICE) #cause we need all of them
        print(ues_number_for_this_lambda)
        print ("******************************************")
        while counter <= ues_number_for_this_lambda:
          selected_ue = random.choice(ues_list)
          if selected_ue in ue_selected: #checking that ues are not repeated
            continue
          else: 
            ue_selected.append(selected_ue)
            ue_state[selected_ue + "_A"] = - (1/lambda_value) * math.log(random.rand()) + slot_time #-(1/lambd)*math.log(random.rand())+slottime
            ue_state[selected_ue + "_D"] = ue_state[selected_ue + "_A"] + service_time() #(-(10)*math.log(random.rand()))   
            list_event(selected_ue,ue_state[selected_ue + "_A"], ue_state[selected_ue + "_D"],iss,register,uplink,downlink,PDU_sRelease,idle,pisss,pregister,puplink,  pdownlink,pPDU_sRelease,pidle,list_to_execute,lambd,contador)#sending the ue's state, and configuration accordingly to first scenarios(it is done for the 3 attack and normal behavior)
            contador+=1 #counting number of selected UEs
        slot_time += INTERVAL_TIME 
        print("counter: " + str(counter))

        list_to_execute.sort(key=takefourth)

        with open('/home/ubuntu/UERANSIM/script/files/BeningList_attack1.txt', 'w') as file:
          for line in list_to_execute:
            file.write(','.join(str(item) for item in line))
            file.write("\n" )

        for i in list_to_execute:
          print(i)
          
        return list_to_execute