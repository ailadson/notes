from Queue import *

def wired_connections(P, W):
    G = build_graph(P, W)
    colors = [None] * len(G)

    for node, edgeList in enumerate(G):
        if colors[node] is None:
            if bfs(G, colors, node) is False:
                return False

    division = { 'L' : [], 'R' : [] }

    for node, color in enumerate(colors):
        if color is 'B':
            division['L'].append(node)
        else:
            division['R'].append(node)

    return division

def build_graph(N, E):
    adj = [[] for i in range(N)]

    for i, edge in enumerate(E):
        adj[edge[0]].append(edge[1])

    return adj

def bfs(G, colors, start):
    colors[start] = 'B'
    q = Queue()
    q.put(start)

    while q.empty() is not True:
        node = q.get()
        for i, neighbor in enumerate(G[node]):
            if colors[neighbor] is None:
                colors[neighbor] = opposite(colors[node])
                q.put(neighbor)
            elif colors[neighbor] is not opposite(colors[node]):
                return False


    return True

def opposite(color):
    return "B" if color is 'W' else 'W'

p = 7
e = [
    [0, 3],
    [1, 2],
    [2, 3],
    [2, 5],
    [3, 4],
    [3, 0],
    [2, 1],
    [3, 2],
    [5, 2],
    [4, 3],
    [6, 5],
    [5, 6],
]

d = wired_connections(p,e)

print d
