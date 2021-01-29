import sys
x, y = [int(i) for i in input().split()]

for a in range(x+1):
    if 2 * a + 4*(x-a) == y:
        print("Yes")
        sys.exit()

print("No")