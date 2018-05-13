import os 
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from mainexecution import invoke_file_changing_handler,add_new_folder_to_watch_list,invoke_file_changing_handler_on_new_folder


class MyFolderChangingHandler(PatternMatchingEventHandler):

    def process_on_modified(self, event):
        print("folder %r has been modified! "%(event.src_path))
        print("we must invoke file changing handler")
        invoke_file_changing_handler(event.src_path)
    
    def on_modified(self, event):
        self.process_on_modified(event)
        

    def process_on_created(self, event):
        if os.path.isdir(event.src_path):
            print("folder %r has been newly created "%(event.src_path))
            add_new_folder_to_watch_list(event.src_path)
            invoke_file_changing_handler_on_new_folder(event.src_path)
        else:
            print(" %r is a file" %(event.src_path))
    
    def on_created(self, event):
        self.process_on_created(event)
        