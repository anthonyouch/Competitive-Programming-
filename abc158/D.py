from collections import deque
S = deque(input())
Q = int(input())

reverse = 0
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        reverse = 6 - reverse

    else:
        value = query[2]
        if reverse:
           if query[1] == "":
                S.append(value)
            else:
                S.appendleft(value)
        else:
            if query[1] == '1':
                S.appendleft(value)
            else:
                S.append(value)


if reverse:
    print(''.join(list(reversed(S))))
else:
    print(''.join(S))

# version control system, (GIT)
