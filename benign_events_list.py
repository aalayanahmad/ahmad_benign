from file_handling import *
from constants import NUMBER_OF_UES_PER_SLICE

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
    creating_ue_file_names(NUMBER_OF_UES_PER_SLICE,1,2,1)# creating yaml files
    creating_ue_file_names(NUMBER_OF_UES_PER_SLICE,2,3,2)
    yamlfiles(NUMBER_OF_UES_PER_SLICE,3,4,3)
    yamlfiles(NUMBER_OF_UES_PER_SLICE,4,5,4)
 
 ueState=dict()#it help to manage the different ue'states through the programm
 uelist=[]#to create the ue pool
 ueselected=[]#to control the number of ues that has been selected.
 list_to_execute=[]
 tempUeList=[]
 toDeleteueState=[]
 

 
 list_of_lambda= [1,3,5,7,8,6,4,2] #[2,4,6,8,10,8,6,4] #[10,25,35,20]#10,20,30,15#[2,4,5,7,9,7,6,4]-[2,4,6,8,10,8,6,4]#[1,2,3,4,5,4,3,2]
 slottime=0.0
 for lambd in list_of_lambda:
  contador=1
  
 
  if lambd>1:
   tempUeList=[ueTemp for ueTemp in ueselected if ueState[ueTemp+"_D"]>=slottime]
   ueselected.clear()
   ueselected=tempUeList.copy()
   print("ueselected list:")
   print(ueselected)
   



  print ("******************************************")
  print(uelist)
  print ("******************************************")


  ue_number=lambd*intervalTime
  uelist=ues_list(10,ueperslice)
  
  print(ue_number)
  print ("******************************************")

  
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