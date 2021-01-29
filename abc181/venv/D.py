from itertools import permutations
import sys

s = input()

hashmap = {}
for i in str(s):
    if i not in hashmap:
        hashmap[i] = 0
    hashmap[i] += 1

if len(s) < 3:
    p = permutations(s)
    for i in p:
        if int("".join(i)) % 8 == 0:
            print("Yes")
            sys.exit()
    print("No")
    sys.exit()


for i in range(104, 1000, 8):
    copy_dic = dict(hashmap)
    valid = 1
    for i in str(i):
        if i not in copy_dic:
            valid = 0
            break

        if copy_dic[i] > 0:
            copy_dic[i] -= 1
        else:
            valid = 0
    if valid == 1:
        print("Yes")
        sys.exit()

print("No")

