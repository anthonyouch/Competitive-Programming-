k = int(input())
string = input()

if len(string) > k:
    print(string[:k] + '...')
else:
    print(string)
