N = int(input())
dishes = [int(i) for i in input().split()]
current_max = 0

for i in range(N):
    current_min = dishes[i]
    for j in range(i,N):
        current_min = min(current_min, dishes[j])
        current_max = max(current_max, current_min * (j-i+1))

print(current_max)