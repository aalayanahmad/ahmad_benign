def ue_yaml_file_names(slice_number, ue_number):
    if (ue_number < 10):
      suffix = f"{slice_number}0{ue_number}" 
    else:
      suffix = f"{slice_number}{ue_number}" 
    file_name = f"ue{suffix}.yaml"
    return suffix, file_name

                             ############################################

def yamlfiles(total_number_of_ues, start, end, flag): #creating all the UEs yaml files
   lines = [] 
   if (flag == 1):
      file_path = "/home/ubuntu/free5gc-compose/config/ue1.yaml" #referece yaml file for other UEs of slice 1
   elif (flag == 2):
      file_path = "/home/ubuntu/free5gc-compose/config/ue2.yaml" #referece yaml file for other UEs of slice 2  
   with open(file_path) as fp:
      lines = fp.readlines()
      for slice_number_x in range(start, end): 
         for ue_number_i in range (0, total_number_of_ues): 
            suffix, file_name = ue_yaml_file_names(slice_number_x, ue_number_i)
            current_imsi = lines[1].strip() #create the imsi according to the network slice
            new_imsi = current_imsi[:-len(suffix)] + suffix
            lines[1] = new_imsi + "\n"
            path = "/home/ubuntu/free5gc-compose/config/"+ file_name
            with open(path, 'w') as fp:
               for line in lines:
                  fp.write(line)

                             ############################################

def takefourth(element):
    return element[2] #return elem[3]