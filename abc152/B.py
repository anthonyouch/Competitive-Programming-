a, b = [int(i) for i in input().split()]
aword = str(a) * b
bword = str(b) * a
print(min(aword, bword))