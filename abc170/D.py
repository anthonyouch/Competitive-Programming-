n = int(input())
lst = [int(i) for i in input().split()]

n = len(lst)

count = 0
for i in range(n):
    valid = True
    for j in range(n):
        if i != j:
            if lst[i] / lst[j] == lst[i] // lst[j]:
                # we know it's invalid
                valid = False
                break
    if valid:
        count += 1

print(count)