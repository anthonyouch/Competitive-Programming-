import sys

n = int(input())

lst = []

for i in range(n):
    a,b = [int(i) for i in input().split()]
    lst.append([a,b])

if len(lst) < 3:
    print("Yes")
    sys.exit()


for ele in lst:
    x1,y1 = ele
    for ele2 in lst:
        x2,y2 = ele2
        for ele3 in lst:
            x3,y3 = ele3
            if ([x1, y1] != [x2, y2] and [x1, y1] != [x3, y3] and [x2, y2] != [x3, y3]):
                if (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
                    print("Yes")
                    sys.exit()

print("No")




