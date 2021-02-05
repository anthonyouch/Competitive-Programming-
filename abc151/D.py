#dfs function given two points find the shortest path to eachother
from time import sleep
H, W = [int(i) for i in input().split()]
board = [[i for i in input()] for j in range(H)]


def dfs(board, start, goal, shortest_path_length):
    # point1 is given in (y,x) (row, column)
    temp = set()
    temp.add(start)
    stack = [(start, temp)]
    deltax = [1,0,-1,0]
    deltay = [0,1,0,-1]
    while stack:
        node, path = stack.pop()
        for i in range(4):
            nxt = (node[0] + deltax[i], node[1] + deltay[i])
            print(path)
            if nxt[0] < 0 or nxt[0] >= H or nxt[1] < 0 or nxt[1] >= W or nxt in path:
                continue
            if len(path) > shortest_path_length:
                continue

            if board[nxt[0]][nxt[1]] == "#":
                continue

            if nxt == goal:
                shortest_path_length = min(shortest_path_length, len(path))
                path.add(nxt)
                ans.append(path)
            path.add(nxt)
            stack.append((nxt, path))

maximum = 0
for i in range(H):
    for j in range(W):
        for x in range(H):
            for y in range(W):
                if i == x and j == y:
                    continue
                if board[x][y] == "#":
                    continue
                start = i,j
                end = x,y
                ans = []
                shortest_path_length = float("inf")
                dfs(board, start, end, shortest_path_length)
                maximum =  max(min(map(len, ans)) - 1, maximum)

print(maximum)





