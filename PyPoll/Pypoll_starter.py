# importing libraries
import csv
import os
# use absolute paths for the files
input_file=os.path.join("Resources", "election_data.csv")
output_file=os.path.join("analysis","election_results.txt")
#initializing all that require variables
total_votes=0
candidate_votes={}
#reading the csv file and executing for loop and if conditions
with open(input_file,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    header=next(csvreader)
    for row in csvreader:
        candidate=row[2]
        total_votes+=1

        if candidate in candidate_votes:
            candidate_votes[candidate]+=1
        else:
            candidate_votes[candidate]=1

winner=max(candidate_votes,key=candidate_votes.get)

# displaying output in the required format
output=(
    "Election Results\n"
    "------------------------\n"
    f"Total Votes: {total_votes}\n"
    "------------------------\n"
)
for candidate, votes in candidate_votes.items():
    percentage=(votes/total_votes)*100
    output+=f"{candidate}: {percentage:.3f}% ({votes})\n"
output+=(
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)
# printing the output
print(output)
with open(output_file,'w') as file:
    file.write(output)


