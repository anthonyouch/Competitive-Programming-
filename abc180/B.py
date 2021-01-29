import math
N = int(input())
x = list(map(int, input().split()))

manhattan_distance = 0
euclidian_distance = 0
cheby_distance = []


for i in range(N):
    manhattan_distance += abs(x[i])
    euclidian_distance += (abs(x[i]) ** 2)
    cheby_distance.append(abs(x[i]))

print(manhattan_distance)
print(math.sqrt(euclidian_distance))
print(max(cheby_distance))

