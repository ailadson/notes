def detect_deadlock(t):
    seen = [False] * len(t)
    processing = [False] * len(t)

    for node in range(len(t)):
        if seen[node] is not True and dfs(t, seen, processing, node, None):
            return True
    return False

def dfs(t, seen, processing, node, from_node):
    processing[node] = True
    seen[node] = True

    for e, edge in enumerate(t[node]):
        if edge is from_node:
            continue
        if processing[edge] or (seen[edge] is not True and dfs(t, seen, processing, edge, node)):
            return True

    processing[node] = False
    return False

g = [
    [1, 3, 2],
    [4, 0],
    [3, 0],
    [0, 2],
    [1]
]

print(detect_deadlock(g))
