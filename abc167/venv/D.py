# create a list that eventually goes back to 1
import sys
n, k = [int(i) for i in input().split()]
lst = [int(i) for i in input().split()]

lst.insert(0, 0)

path = [1]
curr = 1

visited = set()

while True:
    if lst[curr] in visited:
        path.append(lst[curr])
        #print(path)
        index_val = path.index(lst[curr])
        pre_path = path[:index_val + 1]
        path = path[index_val + 1:]
        break

    visited.add(lst[curr])
    path.append(lst[curr])
    curr = lst[curr]

if k <= len(pre_path):
    print(pre_path[k])
    sys.exit()
else:
    k-= (len(pre_path) - 1)

remainder = k  % len(path)
#print(pre_path)
#print(path)

print(path[remainder - 1 ])