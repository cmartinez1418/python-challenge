import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("-------------------")


votes = []
candidates = []
vote_count = []
votes_per_candidate = []
percentages = []


with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:

        votes.append(row[0])

        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
        
        vote_count.append(row[2])
        

#total votes

total_votes = len(votes)
print("Total Votes: " + str(total_votes))
print("-------------------")

   
index = range(len(candidates))
for i in index:
    votes_per_candidate.append(vote_count.count(candidates[i]))


# vote percentages
for number in votes_per_candidate:
    vote_percentage = (number / len(votes)) * 100
    percentages.append(round(vote_percentage, 3))


for i in index:
    print(f"{candidates[i]}: {percentages[i]}% ({votes_per_candidate[i]})")

print("-------------------")

# election winner

winner_percentage = -1000000
winner_index = -1
for index, winner in enumerate(percentages):
    if winner > winner_percentage:
        winner_percentage = winner
        winner_index = index


winner_name = candidates[winner_index]
print("Winner: " + winner_name)


print("-------------------")

output_file = os.path.join("Analysis", "PyPoll_final.csv")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Total Votes", "Candidates", "Percent of Votes", "Winner"])

    writer.writerow([total_votes, candidates, percentages, winner_name])