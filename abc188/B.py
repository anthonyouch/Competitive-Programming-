N = int(input())
Alst = [int(i) for i in input().split()]
Blst = [int(i) for i in input().split()]

total = 0
for i in range(len(Alst)):
    total += Alst[i] * Blst[i]

if total == 0:
    print("Yes")
else:
    print("No")
