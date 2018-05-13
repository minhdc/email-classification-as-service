import os
import time
import setttings

from utils import do_the_classification_job
from watchdog.observers import Observer
from MyFileChangingClassHandler import MyFileChangingClassHandler


def invoke_file_changing_handler(target_folder_path):
    do_the_classification_job(target_folder_path)
    print("done the classifcation job on modified folder")
    pass


def invoke_file_changing_handler_on_new_folder(target_folder_path):
    do_the_classification_job(target_folder_path)
    print("done the classification job on new folder")



def add_new_folder_to_watch_list(folder_path):
    setttings.folder_watch_list.append(folder_path)
    print("successfully added %r to watchlist"%(folder_path))
    print("current wathclist = ",setttings.folder_watch_list)