from math import factorial
from decimal import Decimal
n = int(input()) - 1
k = 11
print(int(Decimal(factorial(n-1)) / Decimal((factorial(11) * factorial(n-12)))))
