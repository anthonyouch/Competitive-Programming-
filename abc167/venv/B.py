import sys
A, B, C, K = [int(i) for i in input().split()]

sum = 0

if A >= K:
    sum = K
    print(sum)
    sys.exit()
else:
    sum += A * 1
    K-= A

if B >= K:
    print(sum)
    sys.exit()
else:
    K-=B

if C >= K:
    sum += K * -1
    print(sum)
    sys.exit()

