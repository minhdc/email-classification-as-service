import os 
import re
import shutil
import setttings

from emailclassification import get_eml_header,get_eml_header_value_by_key



def get_email_address_from_obfuscated_string(input_string):
    print("raw add input string: ",input_string)
    '''
    first_refine = input_string.replace(" ","")
    first_refine = input_string.replace("\n","")
    first_refine = first_refine.replace("\t","")
    second_refine = first_refine.split(' ')
    
    for each_thing in second_refine:
        if len(each_thing) <= 1:
            second_refine.remove(each_thing)
        if '@' not in each_thing:
            second_refine.remove(each_thing)
    '''
    list_of_addr = re.findall(r"<(.*?)>",input_string)
    print("after regexing...",list_of_addr)
    
    '''print("second refine ",second_refine)
    for each_addr in second_refine:
        #if '<' in each_addr:
            each_addr = re.findall(r"<(.*?)>",each_addr)
    print("after second refine : ",second_refine)
    print("then regex: ",list_of_addr)
    if len(second_refine) == len(list_of_addr):'''
    return list_of_addr
    
    
        
    print("email address is cleaan ",input_string)
    return input_string


def create_folder_if_not_exists(parent_path,folder_name):
    #try:      
    
    os.makedirs(os.path.join(parent_path, folder_name),exist_ok=True)
    #print("created storing folder %s at %s" % (folder_name, parent_path))
    
#   except:
#        print("error in creating folder %r "%(os.path.join(parent_path,folder_name)))


def copy_eml_file_to_storing_folder(src_included_eml_file_name,dst):
    #try:
        shutil.copy(src_included_eml_file_name,dst)
        #print("successfully copied %s"%(src_included_eml_file_name))

    #except:
     #   print("copy eml file error, src = %r " %(src_included_eml_file_name))


def get_current_dir_list(curren_path):
    result = [os.path.join(curren_path,x) for x in os.listdir(curren_path)]    
    return result


def do_the_classification_job(eml_file_path):

    list_of_current_file = get_current_dir_list(eml_file_path)
    print("list of current file ",list_of_current_file)
    #print("list of current eml file",list_of_current_file)
    for each_file in list_of_current_file:
        eml_header = get_eml_header(each_file)

        
        base_dst_dir_name = os.path.join(setttings.DST_DIR,os.path.basename(os.path.dirname(each_file)))
        
        #get From Address:
        from_addr_list = get_eml_header_value_by_key(eml_header,"From")
        print("from addr before clean ",from_addr_list)
        from_addr_list = get_email_address_from_obfuscated_string(from_addr_list)        
        print("from addr after clean ",from_addr_list)
        print("file name ",each_file)
        create_folder_if_not_exists(base_dst_dir_name,from_addr_list[0])
        create_folder_if_not_exists(os.path.join(base_dst_dir_name,from_addr_list[0]),"Outbox")
        copy_eml_file_to_storing_folder(each_file,os.path.join(os.path.join(base_dst_dir_name,from_addr_list[0]),"Outbox"))

        #get To address
        to_addr_as_big_string = get_eml_header_value_by_key(eml_header,"To")
        to_addr_as_list = get_email_address_from_obfuscated_string(to_addr_as_big_string)    
        for each_address in to_addr_as_list:
            create_folder_if_not_exists(base_dst_dir_name,each_address)
            create_folder_if_not_exists(os.path.join(base_dst_dir_name,each_address),"Inbox")
            copy_eml_file_to_storing_folder(each_file,os.path.join(os.path.join(base_dst_dir_name,each_address),"Inbox"))


        #get CC address
        cc_addr_as_big_string = get_eml_header_value_by_key(eml_header,"To")
        cc_addr_as_list = get_email_address_from_obfuscated_string(cc_addr_as_big_string)
        for each_address in cc_addr_as_list:
            create_folder_if_not_exists(base_dst_dir_name,each_address)
            create_folder_if_not_exists(os.path.join(base_dst_dir_name,each_address),"Inbox")
            copy_eml_file_to_storing_folder(each_file,os.path.join(os.path.join(base_dst_dir_name,each_address),"Inbox"))

        print("successfully created and copy eml file: %r to folders" %(eml_file_path))
    
    