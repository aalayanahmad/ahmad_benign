import os
from numpy import random
import math
from file_handling import *
from random_event_selection import *
from time_for_event_execution import *
import time

         
# def switching(selectedue,imsi,t,flag,ueSessionId,IdCount):
# #  print(selectedue,imsi)
#   path='/home/ubuntu/UERANSIM/config/'+selectedue
#   deregisterue(imsi,t)#t--------------------  
#   #time.sleep(0.1)
#   with open('/home/ubuntu/UERANSIM/script/files/ue.yaml') as fp:
#     # read an store all lines into list
#     lines = fp.readlines()

#   lines[1]="supi: \'" + imsi + "\'"+ "\n"
# #  deleteonefile(path) #check if this line is need, check when the yaml file is created, it overrides the previous ue's file
  
#   if flag==0:#move to the target slice (from scenario 2: 0=not in the target slcie,1=in the target slice, 2 coming from normal scenario and scenario 1)
#    slicenum=random.choice([1,2,3,4]) #moving to the target slice
#   else: #move back to a different slice
#    print("WRONGGGGGGGGGGGGGGGGG")
#    slicenum=4
    
#   generateyaml(lines,path,slicenum)
#   #time.sleep(0.5)-----------------------------------------------
#   registerue(selectedue,5)# t
#   IdCount["counter"]+=1
#   ueSessionId[selectedue]=IdCount["counter"]#ueID()   
#   print ("FROM SWITCHING, UESESSIONID:"+selectedue+"-----"+str(ueSessionId[selectedue])) 

def ues_list(start, end):
 arr=[]
 for slice_number in range(1,5): #for slice_number in range(1,5):
  for ue_number in range (start, end):
   ue_name = creating_ue_file_names(slice_number,ue_number)
   arr.append(ue_name)
  return arr   


#********************************************************************************************
def listevent_Recent(selectedue,init,end,iss,register,uplink,downlink,PDU_sRelease,idle,pisss,pregister,puplink,pdownlink,pPDU_sRelease,pidle,arr,lambdaV,i):
 arr.append([int(selectedue[2:5]),2,init*1,lambdaV]) 
 return arr

#********************************************************************************************


#********************************************************************************************  
# def non_compromised_ues_events(attaknumber):

#  iss=[1,3,4,5,6]
#  register=[1,3,4,5,6]
#  uplink=[5,6,1,4]
#  downlink=[5,6,1,3]
#  PDU_sRelease=[3,6,1]
#  idle=[3,4]
 
#  pisss=[0.1, 0.2, 0.25, 0.25,0.2]
#  pregister=[0.1, 0.25, 0.25, 0.2,0.2] 
#  puplink=[0.25,0.3,0.2,0.25]
#  pdownlink=[0.3,0.3,0.3,0.1]
#  pPDU_sRelease=[0.45, 0.45,0.1]
#  pidle=[0.5,0.5]

# #******************************
#  #deleteonefile('/home/ubuntu/UERANSIM/script/files/normal_scenario_event.txt')
#  deletefiles('/home/ubuntu/UERANSIM/config/')
#  yamlfiles(ueperslice,1,2,1)# creating yaml files
#  yamlfiles(ueperslice,2,3,2)
#  yamlfiles(ueperslice,3,4,3)
#  yamlfiles(ueperslice,4,5,4)
 
#  ueState=dict()#it help to manage the different ue'states through the programm
#  uelist=[]#to create the ue pool
#  ueselected=[]#to control the number of ues that has been selected.
#  list_to_execute=[]
#  tempUeList=[]
#  toDeleteueState=[]
 

#  uelist=ues_list(10,ueperslice) 
 
#  list_of_lambda=[2,3,5,6,7,5,3,1] 
#  slottime=0.0
#  for lambd in list_of_lambda:
#   contador=1
  
 
#   if lambd>1:
#    tempUeList=[ueTemp for ueTemp in ueselected if ueState[ueTemp+"_D"]>=slottime]
#    ueselected.clear()
#    ueselected=tempUeList.copy()
#    print("ueselected list:")
#    print(ueselected)
   
#   ue_number=lambd*intervalTime# arravals per minute, it value breaks the following loop----------------------------------------------

#   while contador<=ue_number:
#    selectedue = random.choice(uelist)
 
#    if selectedue in ueselected: #checking that ues are not repeated
#     continue
#    else:
#     ueselected.append(selectedue)
#     ueState[selectedue+"_A"]=-(1/lambd)*math.log(random.rand())+slottime #-(1/lambd)*math.log(random.rand())+slottime
#     ueState[selectedue+"_D"]=ueState[selectedue+"_A"]+serviceTime() #(-(10)*math.log(random.rand()))   
#     listevent(selectedue,ueState[selectedue+"_A"],ueState[selectedue+"_D"],iss,register,uplink,downlink,PDU_sRelease,idle,pisss,pregister,puplink,  pdownlink,pPDU_sRelease,pidle,list_to_execute,lambd,contador)#sending the ue's state, and configuration accordingly to first scenarios(it is done for the 3 attack and normal behavior)
#     contador+=1 #counting number of selected UEs
#   slottime+=intervalTime 
#   print("contador:"+str(contador))
  
#  list_to_execute.sort(key=takefourth)


#  with open('/home/ubuntu/UERANSIM/script/files/normal_scenario_event.txt', 'w') as file:
#    for line in list_to_execute:
#     file.write(','.join(str(item) for item in line))
#     file.write("\n" )

#  for i in list_to_execute:
#   print(i)
    
#  return list_to_execute
 









#********************************************************************************************
def idle(id,t):
 print ("id issssssssssssssssss-----:", id)
 os.system('sudo $HOME/UERANSIM/build/nr-cli UERANSIM-gnb-208-93-1 -e \"ue-release '+ str(id) +'\" & sleep '+str(t))
#********************************************************************************************

# def attack_yaml_ues():
#  yamlfilesattack(ueperslice,1,2,1)# creating yaml files
#  yamlfilesattack(ueperslice,2,3,2)
#  yamlfilesattack(ueperslice,3,4,3)
#  yamlfilesattack(ueperslice,4,5,4) 
 
# #*********************************************************
# def creatingnames_ues_attack(slicenum,numberue):
#     if numberue<10:
#       ending=str(slicenum)+"0"+str(numberue) #getting the ending of the yaml file's name
#     else:
#       ending=str(slicenum)+str(numberue) 
#     filename="ueS"+str(1)+ending+".yaml"
#     return filename
# #*******************************************************************************************

# def yamlfilesattack(numues,inits,ends,flag):

# # list to store file lines
#  lines = []
# # read file
 
#  if flag==1:
#   mypahtfile='/home/ubuntu/UERANSIM/attackues/patterns/ue.yaml'
#  elif flag==2:
#   mypahtfile='/home/ubuntu/UERANSIM/attackues/patterns/ue2.yaml'
#  elif flag==3:
#   mypahtfile='/home/ubuntu/UERANSIM/attackues/patterns/ue3.yaml'
#  elif flag==4:
#   mypahtfile='/home/ubuntu/UERANSIM/attackues/patterns/ue4.yaml'
 
 
#  with open(mypahtfile) as fp:
#     # read an store all lines into list
#     lines = fp.readlines()

# # for line in lines:
# #   print (line)


#  for slicenum in range(inits,ends):#for slicenum in range(1,5)this control number of slices
   
#    for numberue in range (0,numues): #this control number of UE per slice, 30 ues per slice, starting from 0
#     filename=creatingnames_ues_attack(slicenum,numberue)
    
#     imsi=lines[1].strip() #creation imsi accordingly to the network slice.
#     newimsi=imsi[:-4]+filename[4:7]+"'"
#     lines[1]=newimsi+"\n"
    
#     path='/home/ubuntu/UERANSIM/attackues/'+filename
# # Write file
#     with open(path, 'w') as fp:
#      for number, line in enumerate(lines):
#       fp.write(line)
      
#     #generateyaml(lines,path,slicenum)  
    
 