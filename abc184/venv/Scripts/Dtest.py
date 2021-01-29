import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())
dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

for i in range(99, -1, -1):
    for j in range(99, -1, -1):
        for k in range(99, -1, -1):
            if i + j + k == 0:
                continue
            dp[i][j][k] += dp[i + 1][j][k] * i / (i + j + k)
            dp[i][j][k] += dp[i][j + 1][k] * j / (i + j + k)
            dp[i][j][k] += dp[i][j][k + 1] * k / (i + j + k)
            dp[i][j][k] += 1

print(dp[A][B][C])