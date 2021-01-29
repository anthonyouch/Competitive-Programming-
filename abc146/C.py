A, B, X = [int(i) for i in input().split()]
def cost(N):
    return A * N + B * len(str(N))

# binary search
left = 0
right = (10 ** 9)

count = 0
while left <= right:
    midpoint = (left + right) // 2
    if midpoint == 0:
        if cost(midpoint) > X:
            print(0)
            exit()
        print(midpoint)

    if cost(midpoint) > X:
        if cost(midpoint - 1) <= X:
            print(midpoint - 1)

            exit()
        right = midpoint - 1
    elif cost(midpoint) <= X:

        if cost(midpoint + 1) > X:
            print(midpoint)
            exit()
        left = midpoint + 1

print(left if left != 1000000001 else left-1)


