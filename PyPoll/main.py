#import dependcies
import csv
from pathlib import Path

#set file path
election_data=Path('./Resources/election_data.csv')

#make empty lists and variable to hold voting data
total_votes=0
candidate_list=[]
candidate_votes=[]


#open file and skip headers
with open (election_data,'r') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

    next(csv_reader)
    
    #count total votes and populate candidate list
    for row in csv_reader:
        
        #count total votes
        total_votes+=1

        #grab each candidate
        candidate=row[2]

        #count each vote for each candidate
        if candidate in candidate_list:
            c_index = candidate_list.index(candidate)
            candidate_votes[c_index]+=1
        else:
            candidate_list.append(candidate)
            candidate_votes.append(1) 
    
percent_of_vote=[]
highest_vote = candidate_votes[0]
high_vote_index = 0
print(total_votes)
print(candidate_list)
print(candidate_votes)

    

    


