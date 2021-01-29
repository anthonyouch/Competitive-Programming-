n = int(input())
maximum = 0
cumul = 0
curr = 0
max_cumul = 0
nums = [int(i) for i in input().split()]

for num in nums:

    curr += max_cumul
    maximum = max(maximum, curr)
    curr -= max_cumul

    curr += (cumul + num) # 2
    cumul = cumul + num # 2

    max_cumul = max(cumul, max_cumul) # 2

    maximum = max(maximum, curr) # 2

print(maximum)

