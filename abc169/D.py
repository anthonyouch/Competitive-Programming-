from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

n = int(input())

lst = sorted(list(factors(n)))[1:]


occurance_lst = [0] * len(lst)



for i in range(len(lst)):
    while n % lst[i] == 0:
        occurance_lst[i] += 1
        n /= lst[i]

count = 0
substract = 1
for num in occurance_lst:
    val = num
    while val != 0:
        val -= substract
        substract += 1
        count += 1


print(count)
