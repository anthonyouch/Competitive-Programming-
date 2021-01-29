import sys
n,m,t = [int(i) for i in input().split()]
lst =[[int(i) for i in input().split()] for j in range(m)]
temp = n
cur_time = 0
for i in range(m):
    n -= lst[i][0] - cur_time
    if n <= 0:
        print("No")
        sys.exit()
    n += lst[i][1] - lst[i][0]
    if n >= temp:
        n = temp
    cur_time = lst[i][1]

n -= t - cur_time

if n <= 0:
    print("No")
    sys.exit()

print("Yes")
