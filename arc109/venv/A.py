import sys
a,b,x,y = [int(i) for i in input().split()]

if a == b:
    print(x)
if a > b:
    #scenerio one use stairs
    dif = a-b - 1 # get to the one above
    ans = dif * y + x
    #scenerio two, use corridors
    dif = (a-b)* 2 - 1
    ans = min(ans, dif * x)
    print(ans)

if a < b:
    # get to the same stair
    # scenerio 1
    dif = b-a
    ans = dif * y + x

    #scenerio 2
    dif = (b-a) * 2 + 1
    ans = min(ans, dif * x)
    print(ans)


