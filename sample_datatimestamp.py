# import time and OS modules to use to build file folder name
from datetime import datetime
import os
# Build string for directory to hold files
# Output Configuration
#   drive_letter = Output device location (hard drive) 
#   folder_name = directory (folder) to receive and store PDF files
drive_letter = r'C:\\'
folder_name = r'downloaded-files-'
folder_time = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
folder_to_save_files = drive_letter + folder_name + folder_time
print(folder_to_save_files)
# IF no such folder exists, create one automatically
if not os.path.exists(folder_to_save_files):
    os.mkdir(folder_to_save_files)

