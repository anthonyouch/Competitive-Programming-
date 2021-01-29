n = int(input())

total = 0

for i in range(n):
    a , b = [int(i) for i in input().split()]
    total += (b* (b+1))//2
    total -= ((a-1)* (a-1+1)//2)

print(total)
