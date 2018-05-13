import os
import time
import setttings

from utils import do_the_classification_job,get_current_dir_list
from watchdog.observers import Observer
from MyFileChangingClassHandler import MyFileChangingClassHandler
import MyFolderChangingHandler


def invoke_file_changing_handler(target_folder_path):
    if target_folder_path in setttings.folder_watch_list:
        do_the_classification_job(target_folder_path)
        print("done the classifcation job on modified folder",target_folder_path)
    else:
        print("%r is not in the current watchlist")
    #pass


def invoke_file_changing_handler_on_new_folder(target_folder_path):
    do_the_classification_job(target_folder_path)
    print("done the classification job on new folder",target_folder_path)


def add_new_folder_to_watch_list(folder_path):
    setttings.folder_watch_list.append(folder_path)
    print("successfully added %r to watchlist"%(folder_path))
    print("current wathclist = ",setttings.folder_watch_list)

'''
def grab_all_current_folder_into_watchlist(parent_path):
    list_of_dir = get_current_dir_list(parent_path)
    for each_dir in list_of_dir:
        make_an_observer(each_dir)
    print("successfully set observer to all folder in watchlist")


def make_an_observer(folder_path):
    observer = Observer()
    observer.schedule(MyFolderChangingHandler(),path = folder_path)
    observer.start()'''