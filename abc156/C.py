N = int(input())
points = [int(i) for i in input().split()]
meeting = round(sum(points) / len(points))
total =  0

for point in points:
    total += ((point - meeting) ** 2)
print(total)