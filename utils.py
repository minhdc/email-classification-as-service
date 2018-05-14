import os 
import re
import shutil
import setttings

from emailclassification import get_eml_header,get_eml_header_value_by_key
from watchdog.observers import Observer


def get_from_address_from_obfuscated_string(input_string):
    if '<' in input_string:
        #return re.findall(r"<(.*?)>",input_string)
        return re.findall(r'[\w\.-]+@[\w\.-]+',input_string)
    else:
        result = []
        result.append(input_string)
        return result


def get_email_address_from_obfuscated_string(input_string):
    #print("raw add input string: ",input_string)
    number_of_email_addr = input_string.count('@')
    print("number of @ ",number_of_email_addr)
    if number_of_email_addr == 1:
        return get_from_address_from_obfuscated_string(input_string)

    #list_of_addr = re.findall("(?:[a-z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*)@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])",input_string)        
    #list_of_addr = re.findall(r"\A[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",input_string)
    
    #using regex
    list_of_addr = re.findall(r'[\w\.-]+@[\w\.-]+',input_string)
    
    print("len of list of addr: ", len(list_of_addr))
    
    if len(list_of_addr) != number_of_email_addr:
        print("[DANGER]missing email address....")
    return list_of_addr
    


def create_folder_if_not_exists(parent_path,folder_name):
    try:
        os.makedirs(os.path.join(parent_path, folder_name),exist_ok=True)
    except PermissionError as e:
        print(e)


def copy_eml_file_to_storing_folder(src_included_eml_file_name,dst):
    try:
        shutil.copy(src_included_eml_file_name,dst)      
    except PermissionError as e:
        print(e)


def get_current_dir_list(curren_path):
    result = [os.path.join(curren_path,x) for x in os.listdir(curren_path)]    
    return result


def do_the_classification_job_for_single_eml_file(eml_file_path):
        eml_header = get_eml_header(eml_file_path)
        dst = os.path.dirname(eml_file_path.replace(setttings.SRC_DIR,setttings.DST_DIR))
        print("dst = ",dst)         

        #get From Address:
        from_addr_list = get_eml_header_value_by_key(eml_header,"From")
        print("from addr before clean ",from_addr_list)
        from_addr_list = get_from_address_from_obfuscated_string(from_addr_list)        
        print("from addr after clean ",from_addr_list)
        print("file name ",eml_file_path)
       
        create_folder_if_not_exists(dst,from_addr_list[0])
        create_folder_if_not_exists(os.path.join(dst,from_addr_list[0]),"Outbox")
        copy_eml_file_to_storing_folder(eml_file_path,os.path.join(os.path.join(dst,from_addr_list[0]),"Outbox"))

        #get To address
        to_addr_as_big_string = get_eml_header_value_by_key(eml_header,"To")
        to_addr_as_list = get_email_address_from_obfuscated_string(to_addr_as_big_string)    
        for each_address in to_addr_as_list:
            create_folder_if_not_exists(dst,each_address)
            create_folder_if_not_exists(os.path.join(dst,each_address),"Inbox")
            copy_eml_file_to_storing_folder(eml_file_path,os.path.join(os.path.join(dst,each_address),"Inbox"))


        #get CC address
        cc_addr_as_big_string = get_eml_header_value_by_key(eml_header,"CC")
        if cc_addr_as_big_string is not None:
            print("this eml has CC too :3 ")
            cc_addr_as_list = get_email_address_from_obfuscated_string(cc_addr_as_big_string)
            for each_address in cc_addr_as_list:
                create_folder_if_not_exists(dst,each_address)
                create_folder_if_not_exists(os.path.join(dst,each_address),"Inbox")
                copy_eml_file_to_storing_folder(eml_file_path,os.path.join(os.path.join(dst,each_address),"Inbox"))
        else:
            print("this eml file doesnt have CC")
        print("successfully created and copy eml file: %r to folders" %(eml_file_path))




def do_the_classification_job(eml_file_path):

    list_of_current_file = get_current_dir_list(eml_file_path)
    print("list of current file ",list_of_current_file)
    #print("list of current eml file",list_of_current_file)
    for each_file in list_of_current_file:
        eml_header = get_eml_header(each_file)

        base_dst_dir_name = os.path.join(setttings.DST_DIR,os.path.basename(os.path.dirname(each_file)))
        print("base dst dir name ",base_dst_dir_name)
        #get From Address:
        from_addr_list = get_eml_header_value_by_key(eml_header,"From")
        print("from addr before clean ",from_addr_list)
        from_addr_list = get_from_address_from_obfuscated_string(from_addr_list)        
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

