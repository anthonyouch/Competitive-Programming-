import math
from collections import defaultdict
n = int(input())

lst = defaultdict(int)

count = 0

for i in range(1, n+1):
    for j in range(i, n+1, i):
        lst[j] += 1

    count += i * lst[i]

print(count)