#import dependcies
import csv
from pathlib import Path

#set file path
election_data=Path('./Resources/election_data.csv')

#make empty lists and variable to hold voting data
total_votes=0
candidate_list=[]
candidate_votes=[]
percent_of_vote=[]
high_vote_index = 0


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

#had to keep highest_vote list here to rightly access candidate_votes list
highest_vote = candidate_votes[0]  

#iterate through each candidate and calculate percentage and add to percent of vote list
for c in range(len(candidate_list)):
    percentage = candidate_votes[c]/total_votes*100
    percent_of_vote.append(percentage)

   #conditional to grab the candidate with the highest vote 
    if candidate_votes[c] > total_votes:
        total_votes = candidate_votes[c]
        print(total_votes)
        high_vote_index = c

#calculate winner by indexing the highest vote with matching candidate in candidate list
winner = candidate_list[high_vote_index]

#print to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
for x in range(len(candidate_list)):
    print(f"{candidate_list[x]}: {percent_of_vote[x]:.3f}% ({candidate_votes[x]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#set export file path & send to Analysis folder (found better new line technique)
analysis_file = Path('./Analysis/election_data_analysis.txt')

with open (analysis_file,'w') as export:

    export.write("Election Results\n")
    export.write("--------------------------\n")
    export.write(f"Total Votes: {total_votes}\n")
    for x in range(len(candidate_list)):
        export.write(f"{candidate_list[x]}: {percent_of_vote[x]:.3f}% ({candidate_votes[x]})\n")
    export.write("---------------------------\n")
    export.write(f"Winner: {winner}\n")
    export.write("---------------------------\n")

#close file
export.close()


    

    


