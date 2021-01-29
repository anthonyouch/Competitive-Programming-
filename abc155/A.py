lst = [int(i) for i in input().split()]

dic = {}
for num in lst:
    if num not in dic:
        dic[num] = 0
    dic[num] += 1

for num in dic.values():
    if num == 2:
        print("Yes")
        exit()
print("No")