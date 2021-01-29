n, m = [int(i) for i in input().split()]
lst = [int(i) for i in input().split()]

for num in lst:
    n-= num

if n < 0:
    print('-1')
else:
    print(n)

