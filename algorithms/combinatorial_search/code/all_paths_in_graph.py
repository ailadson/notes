def all_paths(g, s, t):
    n = len(g)
    path = [None] * n
    path[0] = s
    data = {
        'graph' : g,
        'target' : t,
        'n' : n
    }
    backtrack(path, 0, data)


def backtrack(path, step, data):
    if path_found(path, step, data):
        process_solution(path, step, data)
    else:
        step += 1
        next_vertices = construct_next_vertices(path, step, data)
        for i, vertex in enumerate(next_vertices):
            path[step] = vertex
            backtrack(path, step, data)

def path_found(path, step, data):
    return data['target'] == path[step]

def process_solution(path, step, data):
    print path[:step + 1]

def construct_next_vertices(path, step, data):
    in_path = [False] * data['n']
    next_vertices = []

    for i in range(step):
        in_path[ path[i] ] = True

    last_vertex = path[step - 1]

    for i, neighbor in enumerate(data['graph'][last_vertex]):
        if not in_path[neighbor]:
            next_vertices.append(neighbor)

    return next_vertices

g = [
    [1,3,2],
    [0,4],
    [0,3],
    [0,2,4],
    [1,3,5],
    [5]
]

all_paths(g,2,5)
