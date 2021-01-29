n, k = [int(i) for i in input().split()]

lst = sorted([int(i) for i in input().split()])


a = sum(lst[:k])

print(a)


