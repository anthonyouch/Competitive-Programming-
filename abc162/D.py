import math
n = int(input())
s = input()
count = 0
total = 0
for i in range(n):
    for j in range(i+1, n):
        k = 2*j - i
        # count of of all possibiles that satisify the first condition but not the second
        if k < n:
            if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                count += 1

# count of all possibiles that satisify the first condition
for i in range(n):
    for j in range(i+1, n):
        for k in range(j + 1, n):
            if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                total+= 1

print(total - count)
#k = 2*j - i