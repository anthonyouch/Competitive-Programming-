import math
N = int(input())

lst = []
for i in range(1, int(math.sqrt(N)+1)):
    if N % i == 0:
        lst.append(i)
        if int(N/i) != i:
            lst.append(int(N/i))

lst = sorted(lst)
for i in lst:
    print(i)


