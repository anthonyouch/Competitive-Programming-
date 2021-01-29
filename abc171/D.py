
n = int(input())
res = [int(i) for i in input().split()]
dic = {}

for i in res:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1


k = int(input())

sum = 0

for i in dic.keys():
    sum += i* dic[i]


for i in range(k):
    x, y = [int(i) for i in input().split()]

    if x in dic:
        val = dic[x]
        dic[x] = 0
    else:
        val = 0
    if y not in dic:
        dic[y] = val
    else:
        dic[y] += val

    sum += (y*val) - (x*val)

    print(sum)



