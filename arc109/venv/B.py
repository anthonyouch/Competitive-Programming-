import math
from decimal import *
n = int(input())

# see how much the longest n length log can buy
# solve for n

ans = ((Decimal(8*(n+1)+1) ** Decimal(0.5) -1)) // 2

print(n+1-int(ans))

