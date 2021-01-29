N, M = [int(i) for i in input().split()]
import math
#N balls is even
#M balls is odd
#number of balls N + M == even
# to get even we need even + even or odd + odd
# ammount of 2 combinations of even + amount of 2 combinations of odd
amount = 0
if N-2 >= 0:
    amount += math.factorial(N) /  (2 * math.factorial(N - 2))
if M-2 >= 0:
    amount += math.factorial(M) /  (2 * math.factorial(M - 2))
print(int(amount))
