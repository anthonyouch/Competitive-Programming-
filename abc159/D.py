N = int(input())
nums = [int(i) for i in input().split()]
num_dic = {}

for num in nums:
    if num not in num_dic:
        num_dic[num] = 0
    num_dic[num] += 1

#without removing value
dp = [0] * (max(nums) + 1)
for key, value in num_dic.items():
    if value <= 1:
        continue
    dp[key] = (value * (value - 1)) / 2

#with removing one value

dptwo = [0] * (max(nums) + 1)
for key, value in num_dic.items():
    if value <= 2:
        continue
    num_dic[key] -= 1
    dptwo[key] = (num_dic[key] * (num_dic[key] - 1)) / 2
    num_dic[key] += 1

total = sum(dp)

for num in nums:
    answer = 0
    answer += dptwo[num]
    answer += total - dp[num]
    print(int(answer))

