import os
import time
import setttings

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from RootFolderChangingHandler import RootFolderChangingHandler

class ConfigFileChangingHandler(PatternMatchingEventHandler):
    patterns = setttings.CONFIG_FILE_SUFFIX
    modified = False


    def on_modified(self, event):
        self.process_on_modified(event)
        self.modified = True


    def process_on_modified(self, event):         
        config_file = open(event.src_path,"r")
        
        setttings.SRC_DIR = config_file.readline().replace("\n","")
        setttings.DST_DIR = config_file.readline().replace("\n","")
        setttings.CONFIG_FILE_CHANGED = True

        print("%r "%(setttings.SRC_DIR))
        print("%r" %(setttings.DST_DIR))

        self.modified = False
        folder_observer = Observer()
        folder_observer.schedule(RootFolderChangingHandler(),path = setttings.SRC_DIR,recursive=True)
        folder_observer.start()
        #observer = Observer()
        #observer.schedule(RootFolderChangingHandler(),path = setttings.SRC_DIR)
        #observer.start()
        
        
        

        