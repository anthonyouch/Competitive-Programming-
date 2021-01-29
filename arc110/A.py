n = int(input())

"""
for x in range(n, 10 ** 13 + 1):
    ans_found = True
    for y in range(2, n+1):
        if x % y != 1:
            ans_found = False
            break
    if ans_found == True:
        ans = x
        break """


def binarySearch(l, r):

    while l <= r:

        mid = l + (r - l) // 2
        print(mid)
        # Check if x is present at mid
        if ans_found(mid):

            return mid
        # If x is smaller, ignore right half
        else:
            r = mid - 1

    return -1


def ans_found(x):
    ans_found = True

    for y in range(2, n + 1):
        if x % y != 1:
            ans_found = False
            break
    return ans_found

temp = n
if n % 2 != 0:
    temp += 1


print(binarySearch(temp, 10** 13))