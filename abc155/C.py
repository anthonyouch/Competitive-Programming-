N = int(input())
votes = [input() for _ in range(N)]

dic = {}

for vote in votes:
    if vote not in dic:
        dic[vote] = 0
    dic[vote] += 1

max_votes = max(dic.values())

votes_order = sorted(dic.items(), key = lambda x: (-x[1], x[0]))

for vote, vote_amount in votes_order:
    if vote_amount == max_votes:
        print(vote)
