N = int(input())
lst = [input().split() for i in range(N)]
count = 0
for i in range(N):
    for j in range(i+1, N):
        # find slope
        slope = (int(lst[j][1]) - int(lst[i][1])) / (int(lst[j][0]) - int(lst[i][0]))
        if slope >= -1 and slope <= 1:
            count += 1

print(count)