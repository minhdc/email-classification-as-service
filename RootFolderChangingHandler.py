import os 
import setttings

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from utils import do_the_classification_job_for_single_eml_file

class RootFolderChangingHandler(PatternMatchingEventHandler):

    def on_created(self, event):
        self.process_on_created(event)
        pass

    def process_on_created(self,event):
        #print("[Root folder handler] has been created :%r" %(event.src_path))
        if ".eml" in event.src_path:
            #print("I will call the eml handler")
            do_the_classification_job_for_single_eml_file(event.src_path)       
        pass

    def on_modified(self, event):
        self.process_on_modified(event)
        pass

    def process_on_modified(self,event):
        #print("[Root folder handler] has been modified : %r" %(event.src_path))
        pass

    def on_deleted(self, event):
        self.process_on_deleted(event)
        pass

    def process_on_deleted(self,event):
        #print("[Root folder handler] has been deleted : %r" %(event.src_path))
        pass