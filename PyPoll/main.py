#import dependcies
import csv
from pathlib import Path

#set file path
election_data=Path('./Resources/election_data.csv')

#make empty lists and variable to hold voting data
total_votes=0



#open file and skip headers
with open (election_data,'r') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

    next(csv_reader)
    
    #count total votes and populate candidate list
    for row in csv_reader:
        
        #count total votes
        total_votes+=1

        #add candidates to candidate list
        candidate_list.append(row[2])

    #extract each candidate's vote count & divide by total votes for percent
    khan= [x for x in candidate_list if x=="Khan"] 
    print(len(khan))
    khan_percent = len(khan)/total_votes
    print(khan_percent)

    li= [x for x in candidate_list if x=="Li"] 
    print(len(li))
    li_percent = len(li)/total_votes
    print(li_percent)

    correy= [x for x in candidate_list if x=="Correy"] 
    print(len(correy))
    correy_percent = len(correy)/total_votes
    print(correy_percent)

    o_tooley= [x for x in candidate_list if x=="O'Tooley"] 
    print(len(o_tooley))
    o_tooley_percent = len(o_tooley)/total_votes
    print(o_tooley_percent)

if khan_percent>li_lercent and khan_percent>correy_percent and khan_percent>o_tooley_percent:
    

    


