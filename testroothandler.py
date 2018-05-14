import time
import sys
import setttings

import tkinter

from RootFolderChangingHandler import RootFolderChangingHandler
from utils import get_current_dir_list
from watchdog.observers import Observer

def show_entry_field():
    print(text_entry_1.get())
    setttings.SRC_DIR = text_entry_1.get()
    print(text_entry_2.get())
    setttings.DST_DIR = text_entry_2.get()

    setttings.folder_watch_list = get_current_dir_list(setttings.SRC_DIR)        
    observer = Observer()
    observer.schedule(RootFolderChangingHandler(), path = setttings.SRC_DIR)
    observer.start()


if __name__ == '__main__':
    print("shit")

    top = tkinter.Tk()
    tkinter.Label(top, text = "INPUT: ").grid(row = 0)
    tkinter.Label(top, text = "OUTPUT: ").grid(row = 1)

    text_entry_1 = tkinter.Entry(top)
    text_entry_2 = tkinter.Entry(top)

    text_entry_1.grid(row = 0, column = 1)
    text_entry_2.grid(row = 1, column = 1)

    tkinter.Button(top, text='SET', command=show_entry_field).grid(row=3, column=2,pady=4)
    top.mainloop()
    

    
    #grab_all_current_folder_into_watchlist(setttings.folder_watch_list)
    #toggle = True
    
    
   