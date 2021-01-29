n , x = [int(i) for i in input().split()]
string = input()

count = x

for i in string:
    if i == 'o':
        count +=1
    else:
        if count != 0:
            count -= 1

print(count)