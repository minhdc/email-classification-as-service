import os
from email import message_from_file


def get_eml_header(eml_file_path):
    return message_from_file(open(eml_file_path,"r",encoding="ISO-8859-1"))._headers


def get_eml_header_value_by_key(eml_header,key_to_search):
    for k , v in eml_header:
        if k == key_to_search:
            return v
    return None


