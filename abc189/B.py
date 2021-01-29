from decimal import Decimal
N, X = [int(i) for i in input().split()]
liquors = [[int(i) for i in input().split()] for i in range(N)]

current_bac = 0
for i in range(len(liquors)):
    liquor = liquors[i]
    current_bac += Decimal(liquor[0] * Decimal(liquor[1]) / Decimal(100))
    if current_bac > X:
        print(i+1)
        exit()

print(-1)