# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
txtpath = os.path.join('.', 'analysis', 'election_results.txt')

total_votes = 0
candidate_list = []
candidate_dict = {}
winner_list = ["yo momma", 0]


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_dict[candidate] = 0
        candidate_dict[candidate] = candidate_dict[candidate] + 1
        

output = (
    f"Election Results\n"
    f"---------------------\n"
    f"Total Votes: {total_votes}\n"
    f"---------------------\n"
)
with open(txtpath,"w") as txtfile:
    txtfile.write(output)
    print(output)

    for name in candidate_list:
        votes = candidate_dict.get(name)
        percentage = float(votes) / float(total_votes) * 100
        output = f"{name}: {percentage:.3f}% ({votes})\n"
        txtfile.write(output)
        print(output)
        if votes > winner_list[1]:
            winner_list[1] = votes
            winner_list[0] = name
    output = (
        f"---------------------\n"
        f"Winner: {winner_list[0]}\n"
        f"---------------------\n"
    )
    txtfile.write(output)
    print(output)
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------