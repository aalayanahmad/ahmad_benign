#from constants import NUMBER_OF_UES_PER_SLICE

def ue_yaml_file_names(slice_number, ue_number):
    if (ue_number < 10):
      suffix = f"{slice_number}0{ue_number}" 
    else:
      suffix = f"{slice_number}{ue_number}" 
    file_name = f'ue{suffix}.yaml'
    return suffix, file_name

                             ############################################

def create_yaml_files(total_number_of_ues_per_slice, slice_number): #creates all the UE yaml files
   
   #choose the appropriate yaml file
   if (slice_number == 1):
      file_path = "./template yaml files/slice1_ue_template.yaml" #referece yaml file for other UEs of slice 1
   elif (slice_number == 2):
      file_path = "./template yaml files/slice2_ue_template.yaml" #referece yaml file for other UEs of slice 2
   elif (slice_number == 12):
      file_path = "./template yaml files/slice12_ue_template.yaml" #referece yaml file for other UEs of slice 1 and 2. THIS IS NOT 12 IN THE FILE NAME, IT JUST MEANS UE BELONGS TO SLICE 1 AND 2
   
   lines = [] 
   with open(file_path) as fp:
      lines = fp.readlines()
      for ith_ue in range (0, total_number_of_ues_per_slice): 
         #create the file name
         suffix, file_name = ue_yaml_file_names(slice_number, ith_ue)

         #modify the imsi
         current_imsi = lines[1].strip() #modify the imsi of the ith ue
         x = -4 if len(suffix) == 3 else -5
         new_imsi = current_imsi[:x] + suffix + "'\n"
         lines[1] = new_imsi 

         #write into the file
         path = "./ues/" + file_name
         with open(path, 'w') as fp:
            for line in lines:
               fp.write(line)

#create_yaml_files(NUMBER_OF_UES_PER_SLICE, 1) #creates the yaml files for the UEs of slice 1
#create_yaml_files(NUMBER_OF_UES_PER_SLICE, 2) #creates the yaml files for the UEs of slice 2

                             ############################################

def take_fourth(element):
     return element[2]