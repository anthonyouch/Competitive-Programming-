info = list(map(int, input().split()))

X = info[0]
Y = info[1]
A = info[2]
B = info[3]

count = 0

while X < Y:
    if (((X * A) - X) < B):
        count += 1
        X = X * A
    else:
        break

count += ((Y - X) // B)

if (Y - X) % B == 0:
    count-= 1

print(count)