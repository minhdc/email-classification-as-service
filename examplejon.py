import os
import emailclassification
import utils
import re

eml_root_path = "D:\\Ubuntu lap trinh\\CPC\\Inbox!1\\"

list_of_eml = utils.get_current_dir_list(eml_root_path)

for eml_path in list_of_eml:
    header = emailclassification.get_eml_header(eml_path)

    x_app_to = emailclassification.get_eml_header_value_by_key(header,"X-Apparently-To")

    print(x_app_to)
    addr = re.findall(r'[\w\.-]+@[\w\.-]+',x_app_to)
    print(addr)
    print("_____")