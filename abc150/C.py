from itertools import permutations
N = int(input())
aperm = tuple(int(i) for i in input().split())
bperm = tuple(int(i) for i in input().split())

lst = [i for i in range(1,N+1)]

perms = permutations(lst)
aindex = 0
bindex = 0
index = 1
for perm in perms:
    if perm == aperm:
        aindex = index
    if perm == bperm:
        bindex = index
    index += 1

print(aindex-bindex) if aindex-bindex >= 0 else print(-(aindex - bindex))