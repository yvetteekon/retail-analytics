# Set paths
import os
import pandas as pd

import datetime as dt
import calendar
calendar.setfirstweekday(calendar.SUNDAY)  
today = dt.datetime.today().strftime("%Y.%m.%d")


def create_directories(destination_path, access_code=777):
    '''
    Creates directories and subdirectories (if they don't exist already).
    
    Returns
    -------
    Indicates directories and subdirectories which already exist or were created because they didn't exist.
    
    '''
    # Create directory
    dir_name_list = ['deliverables', 'deprecated', 'dictionary',  'visualizations']
    for dir_name in dir_name_list:
    
        # Create target Directory if don't exist
        if not os.path.exists(os.path.join(destination_path, dir_name)):
            os.mkdir((os.path.join(destination_path, dir_name)), access_code)
            print("Directory " , dir_name ,  " created ")
        else:    
            print("Directory " , dir_name ,  " already exists")

    sub_dir_list = ['data/raw', 'data/interim', 'data/external', 'data/processed']
    for sub_dir in sub_dir_list:

        # Create target directory & all intermediate directories if don't exists
        if not os.path.exists(os.path.join(destination_path, sub_dir)):
            os.makedirs((os.path.join(destination_path, sub_dir)), access_code)
            print("Subdirectory " , sub_dir ,  " created ")
        else:    
            print("Subdirectory " , sub_dir ,  " already exists")

