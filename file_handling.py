import os

def filelist(pathfiles):
   arrf=[]
   with os.scandir(pathfiles) as entries:
      for entry in entries:
         arrf.append(entry)
         return arrf

def creating_ue_file_names(slice_number, ue_number):
    if (ue_number < 10):
      append_to_end = str(slice_number) + "0" + str(ue_number) #getting the ending of the yaml file's name
    else:
      append_to_end = str(slice_number) +str(ue_number) 
    file_name = "ue" + append_to_end + ".yaml"
    return file_name


def yamlfiles(total_number_of_ues, start, end, flag):
   lines = [] 
   
   if (flag == 1):
      file_path = '/home/ubuntu/UERANSIM/script/ue.yaml' #ASK
   elif (flag == 2):
      file_path = '/home/ubuntu/UERANSIM/script/ue2.yaml'
   
   with open(file_path) as fp:
      # read an store all the lines in a list
      lines = fp.readlines()

   for slice_number_x in range(start, end): #runs for as many slices we have
      for ue_number_i in range (0, total_number_of_ues): #runs for how many ues there are per slice
         filename = creating_ue_file_names(slice_number_x, ue_number_i)
         imsi = lines[1].strip() #create the imsi according to the network slice
         new_imsi = imsi[:-4] + filename[2:5]+ "'"
         lines[1] = new_imsi + "\n"
         path = '/home/ubuntu/free5gc-compose/config/'+ filename

         #write file
         with open(path, 'w') as fp:
            for number, line in enumerate(lines):
               fp.write(line)

def takefourth(elem):
    #return elem[3]
    return elem[2]