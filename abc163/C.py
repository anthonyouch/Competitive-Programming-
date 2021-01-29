n = int(input())
lst = [int(i) for i in input().split()]
dp= [0] * (n + 1)

for num in lst:
    dp[num] += 1

for i in range(1,n+1):
    print(dp[i])

