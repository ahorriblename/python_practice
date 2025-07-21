"""
The first line contains the number of records. After that, each entry contains
the name of the candidate and the number of votes they got in some state.
Count the results of the elections: sum the number of votes for each
candidate. Print candidates in the alphabetical order.
"""

# get num of records
records_num = int(input())
candidate_votes = {}

for i in range(records_num):
    name, votes = input().split()
    votes = int(votes)

    if name in candidate_votes:
        candidate_votes[name] += votes
    else:
        candidate_votes[name] = votes

# expression for i in sequence
# print names in alphabetical order
vote_list = [[0,0] for i in range(len(candidate_votes))]
i = 0

for name, votes in candidate_votes.items():
    vote_list[i][0] = name
    vote_list[i][1] = votes
    i += 1

vote_list.sort()
for candidate in vote_list:
    print(*candidate)