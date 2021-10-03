# Worked on this section of the assignment with the Tutor(Cedric Lutonda)
# Create the file path across operating systems
import os

# The module for reading csv file
import csv

# The path for the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# Use the Improved Reading using CSV module
# Create a dictionary to hold the candidates names
candidate_votes = dict()

# Create a list of candidates that we find in the csv file
# key = candidate; value = vote
candidates_list = []

# Initialze the total votes to zero
total_votes = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # For each row add one to the number of votes for a total vote count
        total_votes+=1

        # Check to see the candidates name in column 3
        candidate=row[2]

        # If candidate is not in the list then add the candidate to the candidates_list
        if candidate not in candidates_list: 
            candidates_list.append(candidate)

        # Add the candidate to the dictionary if not already in the dictionary
            candidate_votes[candidate]=0

        # Once candidate is already in the list then increase the vote by one for the candidate each time the name is in colum 3
        candidate_votes[candidate]+=1
        
# Print the results for the election
print(f'Election Results')
print(f'-------------------------')
# Total # of votes casted
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
# Print the name of each candidate, followed by the percentage of votes received, and then print the total votes received
for candidate in candidates_list:
    candidate_percentage = (candidate_votes[candidate]/total_votes)*100
    print(f'{candidate}: {candidate_percentage:.3f}% ({candidate_votes[candidate]})')
print(f'-------------------------')
# Calculate the winner of the election
# Reviewed webiste (https://datagy.io/python-get-dictionary-key-with-max-value/)
winner = max(candidate_votes,key=candidate_votes.get)
# Print the election winner
print(f'Winner: {winner}')
print(f'-------------------------')

# Learnt to write text files with Tim Smith in study group
# Reviewed website (https://www.pythontutorial.net/python-basics/python-write-text-file/#:~:text=To%20write%20to%20a%20text%20file%20in%20Python%2C,close%20the%20file%20using%20the%20close%20%28%29%20method)
# Specify the file to write  the text to
output_path = os.path.join("analysis", "PyPollAnalysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as f:

   # Save the results printed earlier in the text file
    f.write(f'Election Results \n')
    f.write(f'------------------------- \n')
    f.write(f'Total Votes: {total_votes} \n')
    f.write(f'------------------------- \n')
    for candidate in candidates_list:
        candidate_percentage = (candidate_votes[candidate]/total_votes)*100
        f.write(f'{candidate}: {candidate_percentage:.3f}% ({candidate_votes[candidate]}) \n')
    f.write(f'------------------------- \n')
    winner = max(candidate_votes,key=candidate_votes.get)
    f.write (f'Winner: {winner} \n') 
    f.write(f'------------------------- \n')
