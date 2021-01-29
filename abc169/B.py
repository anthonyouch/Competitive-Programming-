import sys
n = int(input())
lst = [int(i) for i in input().split()]

lst.sort()
if lst[0] == 0:
    print(0)
    sys.exit()
sum = 1
for i in lst:
    sum *= i
    if sum > 10 ** 18:
        print(-1)
        sys.exit()
print(sum)