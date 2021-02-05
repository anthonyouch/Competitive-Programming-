def combination_num(n, r):
    if n == r:
        return 1
    mod = 10 ** 9 + 7
    cal = 1
    for i in range(r):
        cal = (cal * (n - i) * pow(r - i, -1, mod)) % mod
    return cal


X, Y = map(int, input().split())


def main():
    if (X + Y) % 3 == 0 and X <= 2 * Y <= 4 * X:
        a = (X + Y) // 3
        b = min(abs(a - X), abs(a - Y))
        print(combination_num(a, b))

    else:
        print(0)


main()