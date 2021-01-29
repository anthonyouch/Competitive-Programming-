# start = [98, 99 ,99]
import queue
import sys
from functools import *



def log(*args):
    for arg in args+('\n',):
        print(arg, file = sys.stderr, end = ' ', flush = True)



def bfs(start, goal):

    q = queue.Queue()
    q.put((start))


    #check for duplicatates
    closed_set = set()

    #res = []
    ans = 0

    if all(goal[i] == start[i] for i in range(len(goal))):
        print(1)

    dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

    dp[99][99][99] = 1

    while not q.empty():
        state = q.get()
        #add nbrs
        for z in range(3):
                nbrs = state[:]
                if goal[z] < nbrs[z]:
                    nbrs[z] -= 1

                    i, j, k = nbrs

                    if dp[i][j][k] == 0:
                        q.put(nbrs)

                        dp[i][j][k] += dp[i + 1][j][k] * i / (i + j + k)
                        dp[i][j][k] += dp[i][j + 1][k] * j / (i + j + k)
                        dp[i][j][k] += dp[i][j][k + 1] * k / (i + j + k)
                        dp[i][j][k] += 1
                        log((i,j,k), dp[i][j][k])
                        # goal_check
                        if all(goal[z] == nbrs[z] for z in range(len(goal))):
                            return dp[nbrs[0]][nbrs[1]][nbrs[2]]


lst = [int(i) for i in input().split()]
start = [99, 99, 99]
print(bfs(start, lst))