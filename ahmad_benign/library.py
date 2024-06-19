import os
from numpy import random
import math
from random_event_selection import *
import time

ues_per_slice = 150 #i have two slices so 150 per slice is enough
interval_time = 15.0 
service_time = 12 #the maximum amount of time a UE can spend in the network per time slot!    
events_per_minute = 15

processing_time_per_event = { "register": 10, "uplink": 2, "downlink": 2, "PDU_sRelease": 5, "idle": 0, "deregister": 2 }
#******************************************************************************************* 
def filelist(pathfiles):
 arrf=[]

 with os.scandir(pathfiles) as entries:
    for entry in entries:
        arrf.append(entry)
 return arrf

#******************************************************************************************* 
def creatingnames(slicenum,numberue):
    if numberue<10:
      ending=str(slicenum)+"0"+str(numberue) #getting the ending of the yaml file's name
    else:
      ending=str(slicenum)+str(numberue) 
    filename="ue"+ending+".yaml"
    return filename
#*******************************************************************************************

def yamlfiles(numues,inits,ends,flag):

# list to store file lines
 lines = []
# read file
 
 if flag==1:
  mypahtfile='/home/ubuntu/UERANSIM/script/ue.yaml'
 elif flag==2:
  mypahtfile='/home/ubuntu/UERANSIM/script/ue2.yaml'
 elif flag==3:
  mypahtfile='/home/ubuntu/UERANSIM/script/ue3.yaml'
 elif flag==4:
  mypahtfile='/home/ubuntu/UERANSIM/script/ue4.yaml'
 
 
 with open(mypahtfile) as fp:
    # read an store all lines into list
    lines = fp.readlines()

# for line in lines:
#   print (line)


 for slicenum in range(inits,ends):#for slicenum in range(1,5)this control number of slices
   
   for numberue in range (0,numues): #this control number of UE per slice, 30 ues per slice, starting from 0
    filename=creatingnames(slicenum,numberue)
    
    imsi=lines[1].strip() #creation imsi accordingly to the network slice.
    newimsi=imsi[:-4]+filename[2:5]+"'"
    lines[1]=newimsi+"\n"
    
    path='/home/ubuntu/UERANSIM/config/'+filename
# Write file
    with open(path, 'w') as fp:
     for number, line in enumerate(lines):
      fp.write(line)

#*******************************************************************************************            
def switching(selectedue,imsi,t,flag,ueSessionId,IdCount):
#  print(selectedue,imsi)
  path='/home/ubuntu/UERANSIM/config/'+selectedue
  deregisterue(imsi,t)#t--------------------  
  #time.sleep(0.1)
  with open('/home/ubuntu/UERANSIM/script/files/ue.yaml') as fp:
    # read an store all lines into list
    lines = fp.readlines()

  lines[1]="supi: \'" + imsi + "\'"+ "\n"
#  deleteonefile(path) #check if this line is need, check when the yaml file is created, it overrides the previous ue's file
  
  if flag==0:#move to the target slice (from scenario 2: 0=not in the target slcie,1=in the target slice, 2 coming from normal scenario and scenario 1)
   slicenum=random.choice([1,2,3,4]) #moving to the target slice
  else: #move back to a different slice
   print("WRONGGGGGGGGGGGGGGGGG")
   slicenum=4
    
  generateyaml(lines,path,slicenum)
  #time.sleep(0.5)-----------------------------------------------
  registerue(selectedue,5)# t
  IdCount["counter"]+=1
  ueSessionId[selectedue]=IdCount["counter"]#ueID()   
  print ("FROM SWITCHING, UESESSIONID:"+selectedue+"-----"+str(ueSessionId[selectedue])) 

def ues_list(init,end):
 arr=[]
 for slice_number in range(1,5): #for slice_number in range(1,5):
  for ue_number in range (init,end):
   ue_name=creatingnames(slice_number,ue_number)
   arr.append(ue_name)
 return arr   
#********************************************************************************************
def time_execution_current_event(current_event):
  if current_event==1:#ISS
   return processtime["iss"]
  elif current_event==2:#registration
   return processtime["register"]
  elif current_event==3:#uplink
   return processtime["uplink"]
  elif current_event==4:#downlink
   return processtime["downlink"]
  elif current_event==5:#pdu session
   return processtime["PDU_sRelease"]
  elif current_event==6:#idle
   return processtime["idle"]
  else: #deregistration 
   return processtime["deregister"]
#********************************************************************************************
def listevent(selectedue,init,end,iss,register,uplink,downlink,PDU_sRelease,idle,pisss,pregister,puplink,pdownlink,pPDU_sRelease,pidle,arr,lambdaV,i):

 print(str(i)+")"+selectedue+" init:"+str(init)+"("+str(init*60)+")"+" end:"+str(end)+"("+str(end*60)+")"+" lda:"+str(lambdaV))
 end_to_seconds=end*60 #pasing minutes to seconds
 #arr.append([selectedue,0,2,init*60,lambdaV,init,0]) #0=deregister,2=register
 arr.append([int(selectedue[2:5]),2,init*60,lambdaV]) #0=deregister,2=register

 currentstate=2
 time=(init*60)#time to control the while structure in seconds
 
 c=0
 while (time<=(end_to_seconds-10)): #(processtime["iss"]+5)
  
  event_to_trigger=randomeventselection(currentstate,iss,register,uplink,downlink,PDU_sRelease,idle,pisss,pregister,puplink,pdownlink,pPDU_sRelease,pidle)#sending the ue's state, and configuration accordingly to first scenarios(it is done for the 3 attack and normal behavior)
  current_event= currentstate
  #poisson=(-(1/(lambdaV+0.1))*math.log(random.rand()))*60 #------------------(-(1/(events_per_minute))*math.log(random.rand()))*60
  poisson=(-(1/(events_per_minute))*math.log(random.rand()))*60 #------------------(-(1/(events_per_minute))*math.log(random.rand()))*60
  if math.floor(poisson)<time_execution_current_event(currentstate):
   p=time+time_execution_current_event(currentstate)
  else:
   p=time+poisson 
  
  
  if (p)<=(end_to_seconds-10):#(processtime["iss"]+5)
   time=p #(poisson+time_execution_current_event(current_event))---------------------
   #arr.append([selectedue,current_event,event_to_trigger,time,lambdaV,poisson,lambdaV+1])
   arr.append([int(selectedue[2:5]),event_to_trigger,time,lambdaV])
   currentstate= event_to_trigger
  else:
   c+=1
  
  if c==3:
   break
 #arr.append([selectedue,currentstate,0,end*60,lambdaV,end,0])   
 arr.append([int(selectedue[2:5]),0,end*60,lambdaV])
  
 return arr
#********************************************************************************************
def listevent_Recent(selectedue,init,end,iss,register,uplink,downlink,PDU_sRelease,idle,pisss,pregister,puplink,pdownlink,pPDU_sRelease,pidle,arr,lambdaV,i):
 arr.append([int(selectedue[2:5]),2,init*1,lambdaV]) 
 return arr
#********************************************************************************************
def takefourth(elem):
    #return elem[3]
    return elem[2]
#********************************************************************************************
def serviceTime():
 while True:
  x=-(servicetime)*math.log(random.rand())#10---------------3 for test with 5 minute long---------------------
  if x>=2 and x<=intervalTime:  #x>8
    break
 return x
# return (-(10)*math.log(random.rand()))

#********************************************************************************************  
def non_compromised_ues_events(attaknumber):

 iss=[1,3,4,5,6]
 register=[1,3,4,5,6]
 uplink=[5,6,1,4]
 downlink=[5,6,1,3]
 PDU_sRelease=[3,6,1]
 idle=[3,4]
 
 pisss=[0.1, 0.2, 0.25, 0.25,0.2]
 pregister=[0.1, 0.25, 0.25, 0.2,0.2] 
 puplink=[0.25,0.3,0.2,0.25]
 pdownlink=[0.3,0.3,0.3,0.1]
 pPDU_sRelease=[0.45, 0.45,0.1]
 pidle=[0.5,0.5]

#******************************
 #deleteonefile('/home/ubuntu/UERANSIM/script/files/normal_scenario_event.txt')
 deletefiles('/home/ubuntu/UERANSIM/config/')
 yamlfiles(ueperslice,1,2,1)# creating yaml files
 yamlfiles(ueperslice,2,3,2)
 yamlfiles(ueperslice,3,4,3)
 yamlfiles(ueperslice,4,5,4)
 
 ueState=dict()#it help to manage the different ue'states through the programm
 uelist=[]#to create the ue pool
 ueselected=[]#to control the number of ues that has been selected.
 list_to_execute=[]
 tempUeList=[]
 toDeleteueState=[]
 

 uelist=ues_list(10,ueperslice) 
 
 list_of_lambda=[2,3,5,6,7,5,3,1] 
 slottime=0.0
 for lambd in list_of_lambda:
  contador=1
  
 
  if lambd>1:
   tempUeList=[ueTemp for ueTemp in ueselected if ueState[ueTemp+"_D"]>=slottime]
   ueselected.clear()
   ueselected=tempUeList.copy()
   print("ueselected list:")
   print(ueselected)
   
  ue_number=lambd*intervalTime# arravals per minute, it value breaks the following loop----------------------------------------------

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


 with open('/home/ubuntu/UERANSIM/script/files/normal_scenario_event.txt', 'w') as file:
   for line in list_to_execute:
    file.write(','.join(str(item) for item in line))
    file.write("\n" )

 for i in list_to_execute:
  print(i)
    
 return list_to_execute
 
#********************************************************************************************  
def ueID():
 deletefiles('/home/ubuntu/UERANSIM/script/commandoutput/') #dete txt file with ps-list information
 os.system('$HOME/UERANSIM/build/nr-cli UERANSIM-gnb-208-93-1 -e ue-list   >> $HOME/UERANSIM/script/commandoutput/ueID.txt')
 
 filetxt= '/home/ubuntu/UERANSIM/script/commandoutput/ueID.txt' 
 with open (filetxt) as f:
  for line in f:
   l=line.strip()
   ueid= l[8:].strip()
   break
   
 return ueid
#********************************************************************************************
def idle(id,t):
 print ("id issssssssssssssssss-----:", id)
 os.system('sudo $HOME/UERANSIM/build/nr-cli UERANSIM-gnb-208-93-1 -e \"ue-release '+ str(id) +'\" & sleep '+str(t))
#********************************************************************************************
def Benign_list():

 iss=[1,3,4,5,6]
 register=[1,3,4,5,6]
 uplink=[5,6,1,4]
 downlink=[5,6,1,3]
 PDU_sRelease=[3,6,1]
 idle=[3,4]
 
 pisss=[0.2, 0.2, 0.2, 0.2,0.2]
 pregister=[0.2, 0.2, 0.2, 0.2,0.2] 
 puplink=[0.25,0.25,0.25,0.25]
 pdownlink=[0.25,0.25,0.25,0.25]
 pPDU_sRelease=[0.33, 0.33,0.34]
 pidle=[0.5,0.5]
 
#******************************
 #deleteonefile('/home/ubuntu/UERANSIM/script/files/normal_scenario_event.txt')
 deletefiles('/home/ubuntu/UERANSIM/config/')
 yamlfiles(ueperslice,1,2,1)# creating yaml files
 yamlfiles(ueperslice,2,3,2)
 yamlfiles(ueperslice,3,4,3)
 yamlfiles(ueperslice,4,5,4)
 
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
#********************************************************************************************

def attack_yaml_ues():
 yamlfilesattack(ueperslice,1,2,1)# creating yaml files
 yamlfilesattack(ueperslice,2,3,2)
 yamlfilesattack(ueperslice,3,4,3)
 yamlfilesattack(ueperslice,4,5,4) 
 
#*********************************************************
def creatingnames_ues_attack(slicenum,numberue):
    if numberue<10:
      ending=str(slicenum)+"0"+str(numberue) #getting the ending of the yaml file's name
    else:
      ending=str(slicenum)+str(numberue) 
    filename="ueS"+str(1)+ending+".yaml"
    return filename
#*******************************************************************************************

def yamlfilesattack(numues,inits,ends,flag):

# list to store file lines
 lines = []
# read file
 
 if flag==1:
  mypahtfile='/home/ubuntu/UERANSIM/attackues/patterns/ue.yaml'
 elif flag==2:
  mypahtfile='/home/ubuntu/UERANSIM/attackues/patterns/ue2.yaml'
 elif flag==3:
  mypahtfile='/home/ubuntu/UERANSIM/attackues/patterns/ue3.yaml'
 elif flag==4:
  mypahtfile='/home/ubuntu/UERANSIM/attackues/patterns/ue4.yaml'
 
 
 with open(mypahtfile) as fp:
    # read an store all lines into list
    lines = fp.readlines()

# for line in lines:
#   print (line)


 for slicenum in range(inits,ends):#for slicenum in range(1,5)this control number of slices
   
   for numberue in range (0,numues): #this control number of UE per slice, 30 ues per slice, starting from 0
    filename=creatingnames_ues_attack(slicenum,numberue)
    
    imsi=lines[1].strip() #creation imsi accordingly to the network slice.
    newimsi=imsi[:-4]+filename[4:7]+"'"
    lines[1]=newimsi+"\n"
    
    path='/home/ubuntu/UERANSIM/attackues/'+filename
# Write file
    with open(path, 'w') as fp:
     for number, line in enumerate(lines):
      fp.write(line)
      
    #generateyaml(lines,path,slicenum)  
    
 