from math import gcd
n = int(input())
sum = 0

for i in range(1,n+1):
    for j in range(1, n+1):
        temp = gcd(i, j)
        for k in range(1, n+1):
            ans = gcd(temp, k)
            sum += ans
print(sum)