import sys
n = input()
total_sum = 0
lst_of_each_remainder = []

for l in n:
    total_sum += int(l)
    if int(l) % 3 > 0:
        lst_of_each_remainder.append(int(l) % 3)

lst_of_each_remainder = sorted(lst_of_each_remainder)


remainder = total_sum % 3


if remainder == 0:
    print(0)
    sys.exit()

if len(n) == 1:
    print(-1)
    sys.exit()


if remainder == 1:
    if lst_of_each_remainder[0] == 1:
        print('1')
        sys.exit()

    if len(n) <= 2:
        print('-1')
        sys.exit()

    if lst_of_each_remainder[-1] == 2 and lst_of_each_remainder[-2] == 2:
        print('2')
    else:
        print('-1')
    sys.exit()


if remainder == 2:
    if lst_of_each_remainder[-1] == 2:
        print('1')
        sys.exit()

    if len(n) <= 2:
        print('-1')
        sys.exit()

    if lst_of_each_remainder[0] == 1 and lst_of_each_remainder[1] == 1:
        print('2')
    else:
        print('-1')


