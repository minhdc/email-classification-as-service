import time
import sys
from MyFileChangingClassHandler import MyFileChangingClassHandler
import MyFolderChangingHandler

from watchdog.observers import Observer

if __name__ == '__main__':
    print("shit")
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyFileChangingClassHandler(), path = args[0])
    observer.start()
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
        print("obsever stopped")

    observer.join()