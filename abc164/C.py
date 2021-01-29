n = int(input())
lst = [input().split() for _ in range(n)]

s = set()
for i in lst:
    s.add(str(i))

print(len(s))