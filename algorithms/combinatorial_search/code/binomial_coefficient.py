def compute_binomial_coefficient(n,k):
    if k >= n:
        return 1
    triangle = [1]
    for i in range(1, n+1):
        for j in reversed(range(1,i+1)):
            if j == i:
                triangle.append(1)
            else:
                triangle[j] = triangle[j - 1] + triangle[j]
    return triangle[k]

print compute_binomial_coefficient(5001, 500)
