import sys
x, n = [int(i) for i in input().split()]

lst = [int(i) for i in input().split()]


if x not in lst:
    print(x)
    sys.exit()
left = x -1
right = x +1

while True:
    if left not in lst:
        print(left)
        sys.exit()
    if right not in lst:
        print(right)
        sys.exit()

    left -= 1
    right +=1




