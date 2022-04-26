# The data we need to retrieve
from sklearn.ensemble import VotingRegressor


#1. The total number of votes cast
#2. A complete list of candidtes who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

file_to_load = 'Resources\election_results.csv.'
with open(file_to_load) as election_data:
    print(election_data)