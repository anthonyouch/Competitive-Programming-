N, K = [int(i) for i in input().split()]
for i in range(10 ** 9):
    if K**i > N:
        print(i)
        exit()