from itertools import combinations
import sys

n, m, x = [int(i) for i in input().split()]
lst = [[]]
for i in range(n):
    lst.append([int(i) for i in input().split()])

# find all combinations of size n to 1
combination_lst = []
for i in range(1,n+1):
    combination_lst.append(i)

final_lst = []

while n > 0:

    comb = combinations(combination_lst, n)

    for tup in comb:
        curr = [0] * (m + 1)
        for ind in tup:
            for i in range(len(lst[ind])):
                curr[i] += lst[ind][i]
        final_lst.append(curr)
    n-= 1

final_lst = sorted(final_lst, key= lambda x: x[0])

for each in final_lst:
    if all(i >= x for i in each[1:]):
        print(each[0])
        sys.exit()

print(-1)

