import sys
dic = {}

n, w  = [int(i) for i in input().split()]

lst = []

for i in range(n):
    lst.append([int(i) for i in input().split()])

array = [0] * (2*100001)

for section in lst:
    array[section[0]] += section[2]
    array[section[1]] -= section[2]

cur  = 0
for num in array:
    cur+= num
    if cur > w:
        print("No")
        sys.exit()
print("Yes")