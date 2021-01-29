n, k = [int(i) for i in input().split()]

dp = [0] * (n + 1)


for i in range(k * 2):
    test = [int(i) for i in input().split()]
    if i % 2 == 0:
        continue
    for index in test:
        dp[index] += 1
sum = 0
for i in dp[1:]:
    if i == 0:
       sum += 1

print(sum)

