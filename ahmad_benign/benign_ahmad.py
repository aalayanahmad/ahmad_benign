from numpy import random
from library import *
#for the benign attack

def benign_list():
    
    #********************************************************************************
    
    #from a register state i can do uplink1,2 (w or w/o issues) downlink, release or idle
    register = [2,3,4,5,6,7,8] #1
    uplink = [7, 8, 3, 4 , 5 , 6] #2 
    uplink_service1 = [7, 8, 3, 4 , 5 , 6] #3 
    uplink_service2 = [7, 8, 2, 4 , 5 , 6] #4
    uplink_service1_with_network_issues = [7, 8, 2, 3, 5 , 6] #5
    uplink_service2_with_network_issues = [7, 8, 2, 3, 4 , 6] #6
    downlink = [7, 8, 2, 3, 4, 5] #7
    pdu_gnb_release = [2, 3, 4, 5, 6, 8] #8
    pdu_ue_release = [2, 3, 4, 5, 6, 8] #9
    idle = [2,3,4,5,6] #10
    deregister = [1] #11
    #********************************************************************************

    #probability of the UE choosing an event_a,b,c (for benign ALL are euqally probable)

    p_register = [0.14,0.14,0.14,0.14,0.14,0.14,0.16] #1
    p_uplink_service1 = [0.16, 0.16, 0.16, 0.16 , 0.16 , 0.2] #2 
    p_uplink_service2 = [0.16, 0.16, 0.16, 0.16 , 0.16 , 0.2] #3
    p_uplink_service1_with_network_issues = [0.16, 0.16, 0.16, 0.16 , 0.16 , 0.2] #4
    p_uplink_service2_with_network_issues = [0.16, 0.16, 0.16, 0.16 , 0.16 , 0.2] #5
    p_downlink=[0.16, 0.16, 0.16, 0.16 , 0.16 , 0.2] #6
    p_pdu_s_release=[0.16, 0.16, 0.16, 0.16 , 0.16 , 0.2] #7
    p_idle=[0.2,0.2,0.2,0.2,0.2] #8
    p_deregister = [1]
    
   #********************************************************************************
    
    #deleteonefile('/home/ubuntu/UERANSIM/script/files/normal_scenario_event.txt')
    # deletefiles('/home/ubuntu/UERANSIM/config/')
    # yamlfiles(ueperslice,1,2,1)# creating yaml files
    # yamlfiles(ueperslice,2,3,2)
    # yamlfiles(ueperslice,3,4,3)
    # yamlfiles(ueperslice,4,5,4)

    ue_state = dict() #to manage the different ue states through the lifecycle of the simulation
    ue_list = [] #to create the ue pool
    ue_selected = [] #to control the number of ues that has been selected.
    list_to_execute = []
    temp_ue_list = []
    to_delete_ue_state=[]


    #arrival time based on a poisson proces
    list_of_lambdas = [1,3,5,7,8,6,4,2] #arrival rates x ue/unit time
    time_slot=0.0
    
    for lambda_value in list_of_lambdas:
        contador=1
        if (lambda_value>1):
            temp_ue_list = [ue_temp for ue_temp in ue_selected if (ue_state[ue_temp+"_D"]>=time_slot)]
            ue_selected.clear()
            ue_selected = temp_ue_list.copy()
        
        
        ue_number = lambda_value * intervalTime #wtf is this
        ue_list = ues_list(10,ueperslice)
        #print(ue_number)
        #print ("******************************************")
    
    
    while contador<=ue_number:
        selectedue = random.choice(uelist)
        if selectedue in ueselected: #checking that ues are not repeated
            continue
        else: 
            ueselected.append(selectedue)
            ueState[selectedue+"_A"]=-(1/lambd)*math.log(random.rand())+slottime #-(1/lambd)*math.log(random.rand())+slottime
            ueState[selectedue+"_D"]=ueState[selectedue+"_A"]+serviceTime() #(-(10)*math.log(random.rand()))   
            listevent(selectedue,ueState[selectedue+"_A"],ueState[selectedue+"_D"],iss,register,uplink,downlink,PDU_sRelease,idle,pisss,pregister,puplink,  pdownlink,pPDU_sRelease,pidle,list_to_execute,lambd,contador)#sending the ue's state, and configuration accordingly to first scenarios(it is done for the 3 attack and normal behavior)
            contador+=1 #counting number of selected UEs
        slottime+=intervalTime 
        print("contador:"+str(contador))
        list_to_execute.sort(key=takefourth)
        
        with open('/home/ubuntu/UERANSIM/script/files/BeningList_attack1.txt', 'w') as file:
            for line in list_to_execute:
                file.write(','.join(str(item) for item in line))
                file.write("\n" )
    
    for i in list_to_execute:
        print(i)
    return list_to_execute