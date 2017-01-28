def total_monotone(k):
    mat = [[1] * k for i in range(9)]

    for i, row in enumerate(mat):
        for j in range(1, k):
            mat[i][j] = cost(mat, i, j)
    # print mat
    return sum_of_paths(mat, k)

def cost(mat, i, j):
    total = 0
    for k in range(i + 1):
        total += mat[k][j - 1]
    return total

def sum_of_paths(mat, k):
    total = 0
    for i in range(9):
        total += mat[i][k-1]
    return total

print total_monotone(1)
