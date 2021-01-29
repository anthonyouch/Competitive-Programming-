n = int(input())
t = int(input())
min_copies = n//3

left_pointer = 0
right_pointer = n

check = "110" * 10
print(check)
count = 0
while right_pointer <= 10*3:
    print(check[left_pointer:right_pointer])
    if check[left_pointer:right_pointer] == str(t):
        count +=1
    right_pointer += n
    left_pointer  += n
print(count)


