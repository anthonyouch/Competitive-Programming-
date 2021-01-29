n, k = [int(i) for i in input().split()]

lst = []

for i in range(n):
    lst.append([int(i) for i in input().split()])

from itertools import permutations
import math

perm_lst = []
for i in range(n):
    perm_lst.append(i)

perm = list(permutations(perm_lst))

total = 0

correct_perms = []

for i in range(len(perm)):
    correct = True
    for j in range(n):
        if perm[i][n-1] != 0:
            correct = False
            break

    if correct == True:
        correct_perms.append(perm[i])

for combo in correct_perms:
    amount  = 0
    next = 0
    for i in range(n):
        amount += lst[next][combo[i]]
        next = combo[i]
    if amount == k:
        total+=1
print(total)