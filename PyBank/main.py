#import dependencies
import csv
import os

#variables for iterating & calculations
total_months=0
net_profit_loss=0
current_month=0
previous_month=0
profit_loss_change=0



#get csv file path and make a variable
from pathlib import Path

budget_data = Path('/Users/Jake/DataClass/python-challenge/PyBank/Resources/budget_data.csv')

#read csv file and print rows
with open(budget_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #grab the header
    
    print(f"CSV Header: {next(csv_reader)}")

    #for row in csv_reader:
        #print(row)
    

    #calculate net income
    for row in csv_reader:
        net_profit_loss = net_profit_loss + int(row[1])
    print(net_profit_loss)
    
    #count total rows without header
    total_months=len(list(csv_reader))
    print(total_months)





