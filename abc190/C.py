from itertools import product
N, M = [int(i) for i in input().split()]
conditions = [[int(i) for i in input().split()] for _ in range(M)]
K = int(input())
people = [[int(i) for i in input().split()] for _ in range(K)]
# brute force every combination
maximum_amount = 0
for roll in product([0, 1], repeat = K):

    index = 0
    temp = set()
    count = 0
    while True:

        temp.add(people[index][roll[index]])
        index += 1
        if index == K:
            break
    for x,y in conditions:
        if x in temp and y in temp:
            count += 1
    maximum_amount = max(maximum_amount, count)
print(maximum_amount)


