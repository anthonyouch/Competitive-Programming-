def find_number_of_factors(num):
    i = 1
    lst = set()
    while i*i <= num:
        if num % i == 0:
            lst.add(i)
            lst.add(int(num/i))
        i+=1
    return len(lst)

count = 0

n = int(input())
for i in range(n+1):
    count += i * find_number_of_factors(i)

print(count)