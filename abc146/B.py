N = int(input())
S = input()
ans = ''
for letter in S:
    coord = ord(letter) - 64 + N
    coord = coord % 26
    if coord == 0:
        ans += "Z"
    else:
        ans += chr(coord + 64)
print(ans)

