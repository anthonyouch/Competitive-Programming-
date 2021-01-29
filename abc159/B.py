S = input()
def check_palindrome(str):
    return str == str[::-1]
if check_palindrome(S):
    midpoint = (len(S) - 1) // 2
    if check_palindrome(S[:midpoint]):
        nextpoint = (len(S) + 3) // 2
        if check_palindrome(S[nextpoint-1:len(S)]):
            print("Yes")
            exit()
print("No")