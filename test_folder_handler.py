import time
import sys
import setttings

from MyFolderChangingHandler import MyFolderChangingHandler
from utils import get_current_dir_list
from watchdog.observers import Observer

if __name__ == '__main__':
    print("shit")
    setttings.folder_watch_list = get_current_dir_list(setttings.SRC_DIR)
    #print(setttings.folder_watch_list)
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyFolderChangingHandler(), path = args[0])
    observer.start()
    toggle = True
    
    try:
        while True:
            time.sleep(1)          
            
    except KeyboardInterrupt:
        observer.stop()
        print("obsever stopped")

    observer.join()