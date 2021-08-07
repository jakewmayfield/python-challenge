#import dependencies
import csv

#get csv file path and make a variable
from pathlib import Path

budget_data = Path('./Resources/budget_data.csv')

#read csv file and print rows
with open(budget_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip header
    next(csv_reader)

    #Make lists for loop data
    total_months=[]
    profit_loss = []
    pl_change = []
    
    
    #loop through data for data and append to lists
    for row in csv_reader:
        
        #total months
        total_months.append(row[0])

        #total profit loss as float for calcs later
        profit_loss.append(float(row[1]))

    # new loop for next month minus this month for month to month change list
    #subtract one from list to keep calculation correct
    for m in range(len(profit_loss)-1):
        pl_change.append(profit_loss[m+1]-profit_loss[m])

    #find greatest increase and decrease using lists & corresponding month by adding 1 to make lists match
    greatest_increase=max(pl_change)
    GI_month=pl_change.index(max(pl_change))+1
    
    greatest_decrease=min(pl_change)
    GD_month=pl_change.index(min(pl_change))+1


#print final figures as Financial Analysis
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: {round(sum(pl_change)/len(pl_change),2)}")
print(f"Greatest Increase in Profits: {total_months[GI_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[GD_month]} (${(str(greatest_decrease))})")

#set path for output file and export (don't forget new line!)
analysis_file = Path('./Analysis/budget_data_analysis.txt')

with open (analysis_file, 'w') as export:
    export.write("Financial Analysis")
    export.write("\n")
    export.write("------------------------")
    export.write("\n")
    export.write(f"Total Months:{len(total_months)}")
    export.write("\n")
    export.write(f"Total: ${sum(profit_loss)}")
    export.write("\n")
    export.write(f"Average Change: {round(sum(pl_change)/len(pl_change),2)}")
    export.write("\n")
    export.write(f"Greatest Increase in Profits: {total_months[GI_month]} (${(str(greatest_increase))})")
    export.write("\n")
    export.write(f"Greatest Decrease in Profits: {total_months[GD_month]} (${(str(greatest_decrease))})")






