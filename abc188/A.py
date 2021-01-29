lst = [int(i) for i in input().split()]
if max(lst) - min(lst) < 3:
    print("Yes")
else:
    print("No")