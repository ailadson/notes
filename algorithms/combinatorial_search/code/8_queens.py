def eight_queens():
    b = Board()
    data = { 'board' : b, 'finished' : False, 'count' : 0 }
    solution = [None] * 8
    backtrack(solution, -1, data)
    print data['count']


def backtrack(solution, step, data):
    if is_solution(solution, step, data):
        process_solution(solution, step, data)
    else:
        step += 1
        next_moves = construct_next_moves(solution, step, data)
        for i, next_move in enumerate(next_moves):
            solution[step] = next_move
            make_move(solution, step, data)
            backtrack(solution, step, data)
            unmake_move(solution, step, data)
            # if data['finished']:
            #     return

def is_solution(solution, step, data):
    return step == 7 # 0-indexed

def process_solution(solution, step, data):
    print data['board']
    data['count'] += 1

def construct_next_moves(solution, step, data):
    return data['board'].open_spaces(step - 1)

def make_move(solution, step, data):
    data['board'].place_queen(solution, step)

def unmake_move(solution, step, data):
    data['board'].remove_queen(solution, step)


class Board:
    def __init__(self):
        self.grid = [[0] * 8 for i in range(8)]
        self.moves = [{ 'x' : None, 'y' : None} for i in range(8)]

    def __str__(self):
        print_str = ""
        for i, row in enumerate(self.grid):
            row_str = "|"
            for j, space in enumerate(row):
                row_str += "{}|".format(space if space == "Q" else " ")
            print_str += "{}\n".format(row_str)
        return print_str

    def place_queen(self, solution, step):
        y, x = solution[step]

        self.moves[step]['x'] = x
        self.moves[step]['y'] = y

        self.block_perp(y, x)
        self.block_diag(y, x)

        self.grid[y][x] = "Q"

    def block_perp(self, y, x):
        for i in range(8):
            self.grid[y][i] += 1
            self.grid[i][x] += 1

    def block_diag(self, y, x):
        for i in range(8):
            if 0 <= y - i < 8 and 0 <= x - i < 8:
                self.grid[y - i][x - i] += 1
            if 0 <= y + i < 8 and 0 <= x - i < 8:
                self.grid[y + i][x - i] += 1
            if 0 <= y - i < 8 and 0 <= x + i < 8:
                self.grid[y - i][x + i] += 1
            if 0 <= y + i < 8 and 0 <= x + i < 8:
                self.grid[y + i][x + i] += 1


    def remove_queen(self, solution, step):
        y, x = solution[step]

        self.grid[y][x] = 2
        self.free_perp(y, x)
        self.free_diag(y, x)

    def free_perp(self, y, x):
        for i in range(8):
            self.grid[y][i] -= 1
            self.grid[i][x] -= 1

    def free_diag(self, y, x):
        for i in range(8):
            if 0 <= y - i < 8 and 0 <= x - i < 8 and self.grid[y - i][x - i] > 0:
                self.grid[y - i][x - i] -= 1
            if 0 <= y + i < 8 and 0 <= x - i < 8 and self.grid[y + i][x - i] > 0:
                self.grid[y + i][x - i] -= 1
            if 0 <= y - i < 8 and 0 <= x + i < 8 and self.grid[y - i][x + i] > 0:
                self.grid[y - i][x + i] -= 1
            if 0 <= y + i < 8 and 0 <= x + i < 8 and self.grid[y + i][x + i] > 0:
                self.grid[y + i][x + i] -= 1

    def open_spaces(self, move_step):
        if move_step < 0:
            start_x, start_y = 0, 0
        else:
            prev_x, prev_y = self.moves[move_step]['x'], self.moves[move_step]['y']
            start_x = prev_x + 1 if prev_x < 7 else 0
            start_y = prev_y if prev_x + 1 <= 7 else prev_y + 1
            if start_y > 7:
                return []

        open_spaces = []
        for i in range(start_y, 8):
            for j in range(8):
                if i == start_y and j < start_x:
                    continue
                if self.grid[i][j] == 0:
                    open_spaces.append([i, j])
        # print (start_x, start_y)
        # print open_spaces
        # print self
        return open_spaces

eight_queens()
