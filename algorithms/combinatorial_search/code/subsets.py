def subsets(arr):
    n = len(arr)
    sets = []
    solution = [None] * n
    data = { 'n' : n, 'process' : lambda x : sets.append(x) }
    backtrack(solution, -1, data)
    return map(lambda s : map(lambda i : arr[i], s), sets)

def backtrack(solution, step, data):
    if is_solution(solution, step, data):
        process_solution(solution, step, data)
    else:
        step += 1
        next_moves = construct_next_moves(solution, step, data)
        for i, next_move in enumerate(next_moves):
            solution[step] = next_move
            # make_move(solution, step, data)
            backtrack(solution, step, data)
            # unmake_move(solution, step, data)

def is_solution(solution, step, data):
    return step is data['n'] - 1

def process_solution(solution, step, data):
    indices = map(lambda (i, exists) : i if exists else exists, enumerate(solution))
    data['process'](filter(lambda e : e is not False , indices))

def construct_next_moves(solution, step, data):
    return [True, False]

print subsets(["lions", "tigers", "bears", "oh my!"])
