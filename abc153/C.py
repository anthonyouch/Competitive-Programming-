N, K = [int(i) for i in input().split()]
health = [int(i) for i in input().split()]
current = sum(health)
health = sorted(health)
for i in range(min(K,len(health))):
    current -= health[-1]
    health.pop()
print(current)
