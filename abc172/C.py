# binary search
def binary_search(num, lst):
    left = 0
    right = len(lst)
    while (left <= right):
        mid = (left + right) // 2
        if lst[mid] > num:
            if mid == 0 or lst[mid-1] < num:
                return mid-1
            else:
                right = mid-1
        elif lst[mid] == num:
            return mid

        elif lst[mid] < num:
            if mid == len(lst) -1 or lst[mid+1] > num:
                return mid
            else:
                left = mid+1

n,k,c = (int(i) for i in input().split())

desk_a = [int(i) for i in input().split()]

desk_b = [int(i) for i in input().split()]


max_count = 0

desk_a_cur = 0
desk_a_cumul =  [0]
for i in desk_a:
    desk_a_cur += i
    desk_a_cumul.append(desk_a_cur)

desk_b_cur = 0
desk_b_cumul = [0]
for i in desk_b:
    desk_b_cur += i
    desk_b_cumul.append(desk_b_cur)


for i in range(len(desk_a_cumul)):
    desk_a_index = i

    val = c - desk_a_cumul[i]

    desk_b_index = binary_search(val, desk_b_cumul)

    if desk_b_index != -1 and desk_a_index != -1:
        max_count = max(max_count, desk_b_index + desk_a_index)

print(max_count)