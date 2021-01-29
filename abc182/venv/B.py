import math

dic = {}

n = int(input())

nums = [int(i) for i in input().split()]

for num in nums:
    for i in range(1, num + 1):
        if num % i == 0:
            if i not in dic:
                dic[i] = 0

            dic[i] += 1

max = 2
max_amount = 0

for i in dic.keys():
    if dic[i] >= max_amount and i >= max:
        max = i
        max_amount = dic[i]

print(max)