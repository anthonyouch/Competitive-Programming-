H = int(input())
temp = H
num = 0
occur = 1
if H == 1:
    print(1)
    exit()
while H != 0:
    print('hi')
    H //= 2
    num += 2 ** occur
    if H == 1:
        break
    occur += 1

print(1+num)
