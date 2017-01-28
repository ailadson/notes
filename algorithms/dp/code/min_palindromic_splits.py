def min_palindromic_splits(string):
    mat = build_mat(string)
    offset = 1
    while offset < len(mat):
        idx = 0
        while idx + offset < len(mat):
            mat[idx][idx + offset] = min_prev_splits(mat, string, idx, idx + offset)
            idx += 1
        offset += 1
    for i, row in enumerate(mat):
        print row
    return mat[0][offset - 1]

def build_mat(string):
    mat = [[-1] * len(string) for i in range(len(string))]
    for i in range(len(mat)):
        mat[i][i] = 0
    return mat

def min_prev_splits(mat, word, i, j):
    if is_palindrome(word, i, j):
        return 0
    else:
        min_c = float('inf')
        for k in range(i, j):
            min_c = min(min_c, mat[i][k] + mat[k + 1][j])
        return min_c + 1

def is_palindrome(word, i, j):
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return word[i] == word[j]

print min_palindromic_splits("t|h|e|w|inni|e|w|i|n|s")
