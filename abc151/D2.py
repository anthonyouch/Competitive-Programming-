# dfs function given two points find the shortest path to eachother
from time import sleep

H, W = [int(i) for i in input().split()]
board = [[i for i in input()] for j in range(H)]

check = False
for i in range(H):
    for j in range(W):
        if board[i][j] != '.':
            check = True


if check == False:
    print(H + W - 2)
    exit()

def dfs(board, start):

    dp = [[float("inf") for i in range(W)] for j in range(H)]
    # point1 is given in (y,x) (row, column)
    stack = [(start, [start])]
    deltax = [1, 0, -1, 0]
    deltay = [0, 1, 0, -1]

    while stack:

        node, path = stack.pop()

        visited = set()
        for i in range(4):

            nxt = (node[0] + deltax[i], node[1] + deltay[i])

            if nxt[0] < 0 or nxt[0] >= H or nxt[1] < 0 or nxt[1] >= W or nxt in visited:
                continue

            if nxt not in visited:
                visited.add(nxt)

            if board[nxt[0]][nxt[1]] == "#":
                continue

            if len(path) > dp[nxt[0]][nxt[1]]:
                continue


            dp[nxt[0]][nxt[1]] = min(len(path), dp[nxt[0]][nxt[1]])

            stack.append((nxt, path + [nxt]))

    max_val = 0

    for i in range(H):
        for j in range(W):
            if dp[i][j] != float('inf'):
                max_val = max(max_val, dp[i][j])
    return max_val


maximum = 0
for i in range(H):
    for j in range(W):
        if board[i][j] == "#":
            continue

        start = i, j

        ans = []

        maxi = dfs(board, start)

        maximum = max(maxi, maximum)

print(maximum)