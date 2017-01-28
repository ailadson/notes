def compute_enclosed(A):
    seen = set()

    for i, row in enumerate(A):
        if i == 0 or i is len(A) - 1:
            for j in range(len(row)):
                color_region(A, seen, i, j, 'W')
        else:
            right = 0
            left = len(row) - 1
            color_region(A, seen, i, right, 'W')
            color_region(A, seen, i, left, 'W')

    for i, row in enumerate(A):
        for j, space in enumerate(row):
            color_region(A, seen, i, j, 'B')



def color_region(A, seen, i, j, color):
    if A[i][j] is 'W' and getId([i, j]) not in seen:
        dfs(A, seen, [i, j], color)

def inBounds(A, entry):
    return 0 <= entry[0] < len(A) and 0 <= entry[1] < len(A[entry[0]])

def dfs(A, seen, entry, color):
    original_color = A[entry[0]][entry[1]]
    seen.add(getId(entry))
    adj = [[1,0], [0,1], [-1,0], [0, -1]]

    for e, edge in enumerate(adj):
        nxt = [entry[i] + edge[i] for i in range(2)]
        if inBounds(A, nxt) and A[nxt[0]][nxt[1]] is original_color:
            if getId(nxt) not in seen:
                dfs(A, seen, nxt, color)

    A[entry[0]][entry[1]] = color

def getId(coord):
    return "{}{}".format(coord[0], coord[1])


mat = [
    ['B','B','B','B'],
    ['W','B','W','B'],
    ['B','W','W','B'],
    ['B','B','B','B']
]

compute_enclosed(mat)
print(mat)
