import sys
k = int(input())
a, b = [int(i) for i in input().split()]
temp = k

while k <= b:
    if k >= a and k <= b:
        print("OK")
        sys.exit()
    k += temp
    if k >= a and k <= b:
        print("OK")
        sys.exit()
print("NG")