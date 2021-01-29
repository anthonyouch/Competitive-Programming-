n, m = [int(i) for i in input().split()]
height = [0]
height.extend([int(i) for i in input().split()])

ab = [[int(i) for i in input().split()] for _ in range(m)]

t = [0] * (n+1)

for i in range(1, n+1):
    t[i] = []

for a,b in ab:
    t[a].append(b)
    t[b].append(a)

sum = 0

for i in range(n+1):
    if i == 0:
        continue
    maximum = 0

    for index in t[i]:
        if height[index] > maximum:
            maximum = height[index]
    if height[i] > maximum:
        sum += 1

print(sum)