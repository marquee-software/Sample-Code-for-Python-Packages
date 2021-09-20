from datetime import datetime

def print_time():
    parser = datetime.now()
    return parser.strftime("%d-%m-%Y %H:%M:%S")

print(print_time())
# output 19-09-2021 15:09:14 
# In Windows filenames, many symbols like \/:? etc are not accepted 