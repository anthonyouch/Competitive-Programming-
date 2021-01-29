N, A, B = [int(i) for i in input().split()]
value = N // (A+B)
remainder = min(N % (A+B), A)
print((value * A) + remainder)
