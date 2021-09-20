import sys 
import os
import csv
import pandas


lst= ['name1@domain.com', 'name2@domain.com', '3name@domain.com', '4name@domain.com', 'name5@domain.com', 'name6@domain.com']

# with csv and '\n'
def write_to_csv(list_of_emails):
    with open('emails1.csv', 'w') as csvfile:
        for domain in list_of_emails:
            csvfile.write(domain + '\n')

write_to_csv(lst)

# with csv and delimiter='\n'
def write_to_csv(list_of_emails):
    with open('emails2.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='\n')
        writer.writerow(list_of_emails)

write_to_csv(lst)

# with csv, , newline='' and delimiter = ','
def write_to_csv(list_of_emails):
    with open('emails3.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(list_of_emails)
write_to_csv(lst)
 

# with csv, newline, and delimiter='\n'
def write_to_csv(list_of_emails):
    with open('emails4.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = '\n')
        writer.writerow(list_of_emails)

write_to_csv(lst)  

# list within list
ListInList = [['name1@domain.com', 'name2@domain.com', '3name@domain.com', '4name@domain.com', 'name5@domain.com', 'name6@domain.com']]

# with csv, newline, and delimiter=','
def write_to_csv(list_of_emails):
   with open('emails5.csv', 'w', newline='') as csvfile:
       writer = csv.writer(csvfile, delimiter='\n')
       writer.writerows(list_of_emails)

write_to_csv(ListInList)


# with pandas dataframe's to_csv 
lst = ['name1@domain.com', 'name1@domain.com', '3name@domain.com', '4name@domain.com', 'name5@domain.com', 'name6@domain.com']
df = pandas.DataFrame(data={"email": lst})
df.to_csv("./emails_pandas.csv", sep=',',index=False)
