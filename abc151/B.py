N, K, M = [int(i) for i in input().split()]
scores = [int(i) for i in input().split()]
current_score = sum(scores)
#(current_score + x) / N == M
x = (M * N) - current_score
if x <= 0:
    print(0)
elif x > K:
    print(-1)
else:
    print(x)