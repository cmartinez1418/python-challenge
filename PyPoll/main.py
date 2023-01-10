import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("-------------------")


votes = []
candidates = []
votes_per_candidate = []

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:

        votes.append(row[0])

        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
        
        votes_per_candidate.append(row[2])
        

#total votes

total_votes = len(votes)
print("Total Votes: " + str(total_votes))
print("--------------------")

#for candidate in candidates:
   # candidates.count(row[2])
    #votes_per_candidate.append(candidate)

#for index, candidate in enumerate(candidates):
    #print(candidate)
     
# for index in candidates:   
print(votes_per_candidate.count(candidates[index]))