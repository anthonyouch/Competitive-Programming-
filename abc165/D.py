import math
from decimal import *
a, b, n = [int(i) for i in input().split()]

x = min(n, b-1)

ans = int(Decimal(a*x / b)) - a * int(Decimal(x/b))
print(ans)