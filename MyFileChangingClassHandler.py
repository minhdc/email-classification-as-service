import os
import time
import sys

import setttings

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from emailclassification import get_eml_header,get_eml_header_value_by_key
from utils import get_email_address_from_obfuscated_string,create_folder_if_not_exists,copy_eml_file_to_storing_folder,do_the_classification_job


class MyFileChangingClassHandler(PatternMatchingEventHandler):
    patterns = ["*.eml"]

    def process_on_created(self, event):
        #do the classification job
        eml_file_path = event.src_path
        print("current working eml file paths;",eml_file_path)
        do_the_classification_job(eml_file_path)
        print("done processing created eml")

    def on_created(self, event):  
        print("new file created at %r "%(event.src_path))      
        self.process_on_created(event)
        return

     