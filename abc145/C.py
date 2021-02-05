from itertools import permutations
from math import sqrt
import math
N = int(input())
lst = [i for i in range(N)]
inputs = [[int(i) for i in input().split()] for i in range(N)]

perms = permutations(lst)

# function to find distance between all towns:
def distance(lst):
    total_distance = 0
    for i in range(1, len(lst)):
        x1, y1 = inputs[lst[i]][0], inputs[lst[i]][1]
        x2, y2 = inputs[lst[i-1]][0], inputs[lst[i-1]][1]
        total_distance += sqrt((x1 - x2) ** 2  + (y1 - y2) ** 2)

    return abs(total_distance)
average = 0
for perm in perms:
    average += (distance(perm))
print(average / math.factorial(N))
