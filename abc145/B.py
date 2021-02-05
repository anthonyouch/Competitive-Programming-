N = int(input())
S = input()
if N % 2 != 0:
    print("No")
else:
    midpoint = int((N / 2))
    if S[:midpoint] == S[midpoint:]:
        print("Yes")
    else:
        print("No")