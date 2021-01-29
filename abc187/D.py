def take_sum(elem):
    return sum(elem) + elem[0]

N = int(input())
inputs = [tuple(map(int, input().split())) for i in range(N)]

# sort it by the sum of the voters
new = sorted(inputs, key = take_sum)
takahashi = 0
aoki = sum(pair[0] for pair in new)

count = 0
while takahashi <= aoki:
    count += 1
    a,b = new.pop()
    takahashi += (a+b)
    aoki -= a

print(count)