import math
A, B = [int(i) for i in input().split()]
ans1 = math.ceil(A / 0.08)
ans2 = math.ceil(B / 0.10)

ans1_range = {i for i in range(ans1, math.ceil((A+1) / 0.08))}

ans2_range = {i for i in range(ans2, math.ceil((B+1) / 0.1))}

if ans1 in ans1_range and ans1 in ans2_range:
    if ans2 in ans1_range and ans2 in ans2_range:
        print(min(ans1, ans2))
    else:
        print(ans1)
elif ans2 in ans1_range and ans2 in ans2_range:
    print(ans2)
else:
    print(-1)

