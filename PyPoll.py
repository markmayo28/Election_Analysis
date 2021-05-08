# The data we need to retrieve and sort.
#1. The total number of votes cast.
#2. A complete list of candidates whe received votes:
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("Resources", "analysis", "election_analysis.txt")

#Declare variables and tools (lists, tuples, dictionaries) that will be used prior to opening the file you will be working in

# Initialize a total vote counter.
total_votes = 0

#Create Candidates list (currently empty)
candidate_options = []

# Create a dictionary to hold candidates and their votes (currently empty)
candidate_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here

    # Read the file object with the reader funtcion.
    file_reader = csv.reader(election_data)

    # Read the header row.

    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        #Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Ignore duplicates by looking to see if the name has already been added to the list.
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list if it is not already there.
            candidate_options.append(candidate_name)
            #Begin tracking that candidates vote count (establishes the dictionary key using "dictionary_name[key]" method)
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1

# Print the candidates vote dictionary.
    print(candidate_votes)

    #Get the percentage of the votes that each candidate received.
    #First iterate through the candidate_options list
    for candidate_name in candidate_votes:
        #retrieve the votes for each candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes (while declaring the variable)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"\n{candidate_name}: {vote_percentage:.1f}%({votes:,})\n")

        #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        print(candidate_results)

        # Determine winning vote count and candidate
       
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
       
         # If true then set winning_count = votes and winning_percent = vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

        winning_candidate_summary = (f"--------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------\n")

    print(winning_candidate_summary)

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.


        #print percentage of vote by candidate to 1 decimal place put ":.1f" after float variable
    #print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")

# 3. Print the total votes.
#print("Total votes cast is " + str(total_votes))
#print("Participating candidates are " + str(candidate_options))

# Get a list of candidates.



    


    


#Close the file
