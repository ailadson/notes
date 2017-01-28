def subset_equal_total(arr, total):
    mat = build_mat(arr, total)
    for i in range(1, len(mat)):
        for j in range(1, total + 1):
            mat[i][j] = is_equal_subset(mat, arr, i, j)

    subset = find_subset(mat, arr)
    subset.reverse()
    return subset

def build_mat(arr, total):
    mat = [[False] * (total + 1) for i in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        mat[i][0] = True
    return mat

def is_equal_subset(mat, arr, i, j):
    return mat[i - 1][j] or \
            (arr[i - 1] <= j and mat[i - 1][j - arr[i - 1]])

def find_subset(mat, arr):
    subset = []
    i, j = len(mat) - 1, len(mat[-1]) - 1

    if mat[i][j] is False:
        return subset

    while i != 0 and 0 < j:
        while 0 <= (i - 1) and mat[i - 1][j]:
            i -= 1
            if i == 0: return subset

        subset.append(arr[i - 1])
        j -= arr[i - 1]
        i -= 1
    return subset

a = [1,3,5,6,7]
print subset_equal_total(a, 15)
