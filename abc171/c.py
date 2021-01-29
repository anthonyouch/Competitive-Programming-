n = int(input())
lst = []
while n > 0:
    n-=1
    val = int(n/26)
    mod = int(n%26)
    lst.append(chr(97+mod))
    n = val

print(''.join(reversed(lst)))
