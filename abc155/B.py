N = int(input())
values = [int(i) for i in input().split()]
for value in values:
    if value % 2 == 0:
        if value % 3 != 0 and value % 5 != 0:
            print("DENIED")
            exit()

print("APPROVED")
