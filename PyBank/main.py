import csv
import os

#get csv file path and make a variable
from pathlib import Path

budget_data = Path('/Users/Jake/DataClass/python-challenge/PyBank/Resources/budget_data.csv')

#set net_income counter to 0
net_income=0

#read csv file and print rows
with open(budget_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #grab the header
    
    print(f"CSV Header: {next(csv_reader)}")

    #for row in csv_reader:
        #print(row)
    

    #calculate net income
    for row in csv_reader:
        net_income = net_income + int(row[1])
    print(net_income)
    
    #count total rows without header
    total_months=len(list(csv_reader))-1
    print(total_months)





