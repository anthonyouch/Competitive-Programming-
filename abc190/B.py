N, S, D = [int(i) for i in input().split()]
for i in range(N):
    x, y = [int(i) for i in input().split()]
    if x < S and y > D:
        print("Yes")
        exit()
print("No")