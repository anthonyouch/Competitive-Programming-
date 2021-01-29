N = int(input())
lst = [int(i) for i in input().split()]
ans = 1
current_min = lst[0]
for num in lst[1:]:
    if num <= current_min:
        ans += 1
        current_min = num
print(ans)


