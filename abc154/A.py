
S, T = [str(i) for i in input().split()]
A, B = [int(i) for i in input().split()]
U = input()
if U == S:
    print(A-1,B)
else:
    print(A, B-1)
