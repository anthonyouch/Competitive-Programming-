a,b,c,d = [int(i) for i in input().split()]

import sys
while True:
    c-=b
    if c <=0:
        print("Yes")
        sys.exit()
    a-=d
    if a <=0:
        print("No")
        sys.exit()