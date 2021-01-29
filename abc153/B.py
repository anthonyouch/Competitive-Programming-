H, N = [int(i) for i in input().split()]
attacks = [int(i) for i in input().split()]
if sum(attacks) >= H:
    print("Yes")
else:
    print("No")
