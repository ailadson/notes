from sudoku_board import Board

def sudoku_solver(grid = None):
    grid = grid or [
        [6,4,3,        7,8,9,        2,5,1],
        [5,1,8,        2,6,3,        4,9,7],
        [7,2,9,        1,5,4,        6,8,3],

        [8,3,5,        6,9,2,        None,None,None],
        [1,None,4,     3,7,8,        None,None,None],
        [2,7,6,        5,4,1,        None,None,None],

        [9,5,2,        8,3,7,        1,4,6],
        [3,6,1,        4,None,5,     9,7,8],
        [4,8,7,        9,1,6,        3,2,5],
    ]
    b = Board(9, grid)
    solution = [None] * (9 * 9)
    data = {
        'finished' : False,
        'board' : b
    }
    print "Starting State"
    print b
    print "=" * 30
    print "End State"
    backtrack(solution, -1, data)

def backtrack(solution, step, data):
    if is_complete(solution, step, data):
        process_solution(solution, step, data)
    else:
        step += 1
        next_moves = construct_next_moves(solution, step, data)
        for i, next_move in enumerate(next_moves):
            solution[step] = next_move
            make_move(solution, step, data)
            backtrack(solution, step, data)
            unmake_move(solution, step, data)
            if data['finished']:
                return

def make_move(solution, step, data):
    board = data['board']
    board.fill_square(step, solution)

def unmake_move(solution, step, data):
    board = data['board']
    board.free_square(step, solution)

def is_complete(solution, step, data):
    return data['board'].free_spaces == 0

def process_solution(solution, step, data):
    print data['board']
    data['finished'] = True

def construct_next_moves(solution, step, data):
    board = data['board']
    candidates = []

    x, y, possible_moves = next_square_constrained(board)

    board.moves[step]['x'] = x
    board.moves[step]['y'] = y

    if x is None and y is None:
        return []

    # possible_moves = possible_values(x, y, board)

    for i in range(10):
        if possible_moves[i]:
            candidates.append(i)

    return candidates

def possible_values(x, y, board):
    return board.get_values_for(x, y)

def next_square_arbitrary(board):
    grid = board.grid

    for y, row in enumerate(grid):
        for x, space in enumerate(row):
            if space is None:
                return (x, y)

    return (None, None)

def next_square_constrained(board):
    grid = board.grid
    const_possible_vals = [True] * 20
    const_x = None
    const_y = None

    for y, row in enumerate(grid):
        for x, space in enumerate(row):
            if space is None:
                possible_vals = board.get_values_for(x, y)
                if len_possible(const_possible_vals) > len_possible(possible_vals):
                    const_possible_vals = possible_vals
                    const_x = x
                    const_y = y
    return (const_x, const_y, const_possible_vals)

def len_possible(possible):
    count = 0
    for i in range(len(possible)):
        if possible:
            count += 1
    return count
