from itertools import count

from sympy import ComputationFailed

## LISTS ##
# my_list = ["Arapahoe","Denver","Jefferson"]
# counties = my_list
# counties.insert(1,"El Paso")
# counties.remove("Arapahoe")
# counties.remove("Denver")
# counties[2] = "Denver"
# counties.append("Arapahoe")

# print(counties)
# print(len(counties))

## TUPLES ##
#counties_tuple = tuple("Arapahoe","Denver","Jefferson")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters.')

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)



# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})
# voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.remove({"county":"Denver", "registered_voters": 463353})
# voting_data.insert(2,{"county":"Denver", "registered_voters": 463353})
# voting_data.insert(3,{"county":"Arapahoe", "registered_voters": 422829})
# print(voting_data)

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)