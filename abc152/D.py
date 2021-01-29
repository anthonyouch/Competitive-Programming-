N = int(input())

dp = [[0] * 10 for i in range(10)]
# occurance of first is row, last is collumn

for i in range(1,N+1):
    first = str(i)[0]
    last = str(i)[-1]
    dp[int(first)][int(last)] += 1

ans = 0
for i in range(10):
    for j in range(10):
       ans += dp[i][j] * dp[j][i]

print(ans)

