import sys
import math

a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]


if (a,b) == (c,d):
    print(0)
elif (a + b == c + d) or (a-b == c-d) or (abs(a-c) + abs(b-d)) <=3:
    print(1)

else:
    if (abs(c-a) == 0 and abs(d-b) <=6) or (abs(c-a) <=6 and abs(d-b) ==0):
        print(2)
        sys.exit()

    distance_apart = abs(c-a) + abs(d-b)

    if abs(c-a) % 2 == 0 and abs(d-b) % 2 == 0:
        print(2)
        sys.exit()

    if abs(c-a) % 2 != 0 and abs(d-b) % 2 != 0:
        print(2)
        sys.exit()


    #if abs((c-a) - (d-b)) <= 3:
        #print(2)
        #sys.exit()
    else:
        ## check to see if diagonal in both ways and check to see if the distance is within 3:
        a2, b2 =  c, (b - abs((c-a)))


        if (a2 + b2 == c + d) or (a2-b2 == c-d) or (abs(a2-c) + abs(b2-d)) <=3:
            print(2)
            sys.exit()

        a2, b2 = c, (b + abs((c - a)))

        if (a2 + b2 == c + d) or (a2-b2 == c-d) or (abs(a2-c) + abs(b2-d)) <=3:
            print(2)
            sys.exit()

        print(3)
