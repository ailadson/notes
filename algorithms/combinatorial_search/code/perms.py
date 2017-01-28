def generate_permutations(arr):
    n = len(arr)
    solution = [None] * n
    perms = []
    data = {
        'n' : n,
        'process' : lambda perm : perms.append(perm),
        'arr' : arr
    }
    backtrack(solution, -1, data)
    return perms

def backtrack(solution, step, data):
    if is_solution(solution, step, data):
        process_solution(solution, step, data)
    else:
        step += 1
        next_candidates = construct_next_candidates(solution, step, data)
        for i, next_candidate in enumerate(next_candidates):
            solution[step] = next_candidate
            backtrack(solution, step, data)

def is_solution(solution, step, data):
    return step == data['n'] - 1

def process_solution(solution, step, data):
    perm = map(lambda idx: data['arr'][idx], solution)
    data['process'](perm)

def construct_next_candidates(solution, step, data):
    in_perm = [False] * data['n']
    candidates = []

    for i in range(step):
        in_perm[ solution[i] ] = True

    for i in range(data['n']):
        if not in_perm[i]:
            candidates.append(i)

    return candidates

print generate_permutations(["cat", "dog", "bear", "lion", "fly"])
