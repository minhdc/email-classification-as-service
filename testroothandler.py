import time
import sys
import setttings

from RootFolderChangingHandler import RootFolderChangingHandler
from utils import get_current_dir_list,count_current_email
from watchdog.observers import Observer
from ConfigFileChangingHandler import ConfigFileChangingHandler
from displayutils import show_warning

if __name__ == '__main__':
    print("shit")
    #setttings.folder_watch_list = get_current_dir_list(setttings.SRC_DIR)        
    
    config_file_observer = Observer()
    file_changing_handler = ConfigFileChangingHandler()
    config_file_observer.schedule(file_changing_handler, path = setttings.CONFIG_FILE_LOC)
    config_file_observer.start()
    show_warning("Vui long ghi thoi gian va so luong thu vao file config.txt")
    

    try:
        while True:
            time.sleep(600)            
            #if file_changing_handler.modified:
            show_warning("Received %r emails in this session" %(count_current_email(setttings.SRC_DIR)))
                
    except KeyboardInterrupt:
        config_file_observer.stop()
    config_file_observer.join()

    #grab_all_current_folder_into_watchlist(setttings.folder_watch_list)
    #toggle = True
    
    
   