from itertools import permutations
import math
def combination_num(n, r):
    if n == r:
        return 1

    cal = 1
    for i in range(r):
        cal = (cal * (n - i) * pow(r - i, -1, (10 ** 9) + 7) % (10 ** 9) + 7)
    return cal

X, Y = [int(i) for i in input().split()]
total = 0
n, m = 0, 0
if (X+Y) % 3 != 0:
    print(0)
    exit()
else:
    # simulaneous equations, solve for n and m
    m = int((2*X-Y)/3)
    n = int(X - (2*m))

r = n
n = m + n
print(combination_num(n,r))


