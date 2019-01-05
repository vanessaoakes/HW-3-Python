#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
import os
import csv

csvpath = os.path.join('election_data.csv')

total_votes = -1
candidates = {}
winner = ""

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #print(csvreader)
  #Loop
    for row in csvreader:
        #print(row)
#The total number of votes cast
        total_votes = total_votes + 1
        if total_votes == 0:
            continue

#A complete list of candidates who received votes
        candidate_name = row[2]
        candidate_votes = 0
        if candidate_name in candidates:
            candidate_votes = candidates[candidate_name]
        candidate_votes += 1
        candidates[candidate_name]=candidate_votes
    print(candidates)


#The percentage of votes each candidate won
    output = "\n"
    output += "Election Results\n"
    output += "----------------------\n"
    output += "Total Votes: " + str(total_votes) + "\n"
    output += "----------------------\n"

    for candidate_name in candidates:
        percentage_votes_won=(candidates[candidate_name])/total_votes


#The total number of votes each candidate won
        percentage = round(percentage_votes_won*100,0)
        output += candidate_name + ": " + str(percentage) + "% (" + str(candidates[candidate_name]) + ")\n"

#The winner of the election based on popular vote.
        if candidates[candidate_name] > (total_votes/2):
            winner = candidate_name

    output += "----------------------\n"
    output += "Winner: " + winner + "\n"
    output += "----------------------\n"


print(output)

  #Election Results
  #------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

file = open("Vanessa Oakes HMWK #3 = PyPoll.txt", "w")
file.write(output)

file.close()
