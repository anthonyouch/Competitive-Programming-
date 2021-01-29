N = int(input())
nums = [int(i) for i in input().split()]
unique_values = set()
for num in nums:
    if num not in unique_values:
        unique_values.add(num)
    else:
        print("NO")
        exit()
print("YES")

