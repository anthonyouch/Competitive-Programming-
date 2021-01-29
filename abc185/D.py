from math import factorial

n = int(input())

k = 12


def binomialCoeff(n, k):
    C = [[0 for i in range(k + 1)] for i in range(n + 1)]

    # Calculate value of Binomial Coefficient in bottom up manner
    for i in range(0, n + 1, 1):
        for j in range(0, min(i, k) + 1, 1):
            # Base Cases
            if (j == 0 or j == i):
                C[i][j] = 1

            # Calculate value using previously stored values
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]


print(binomialCoeff(n - 1, k - 1))