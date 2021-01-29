A, B = [str(i) for i in input().split()]
SA = sum([int(i) for i in A])
SB = sum([int(i) for i in B])
print(max(SA, SB))