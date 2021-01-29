n = int(input())
lst = [int(i) for i in input().split()]

left_pointer = 0
right_pointer = 1

total = 0

while left_pointer < n-2:
    if right_pointer >= n:
        left_pointer += 1
        right_pointer = left_pointer + 1
    total += abs(lst[left_pointer] - lst[right_pointer])
    print(str(lst[left_pointer]) + ' ' + str(lst[right_pointer]))
    right_pointer += 1


print(total)