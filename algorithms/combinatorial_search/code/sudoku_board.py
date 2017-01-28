class Board:
    def __init__(self, dim, grid = None):
        self.dim = dim
        self.grid = grid or [[None] * dim for i in range(dim)]
        self.moves = [{ 'x' : None, 'y' : None} for i in range((dim * dim))]
        self.free_spaces = 0

        for i, row in enumerate(self.grid):
            for j, space in enumerate(row):
                if space is None:
                    self.free_spaces += 1



    def get_values_for(self, x, y):
        eligible = [True] * (self.dim + 1)
        eligible[0] = False
        upper_x, upper_y = x/(self.dim/3) * 3, y/(self.dim/3) * 3

        self.check_column_and_row(x, y, eligible)
        self.check_local_box(upper_x, upper_y, eligible)

        return eligible

    def check_column_and_row(self, x, y, eligible):
        for i in range(self.dim):
            if self.grid[i][x] is not None:
                eligible[ self.grid[i][x] ] = False
            if self.grid[y][i] is not None:
                eligible[ self.grid[y][i] ] = False

    def check_column(self, x, eligible):
        for i in range(self.dim):
            if self.grid[i][x] is not None:
                eligible[ self.grid[i][x] ] = False

    def check_row(self, y, eligible):
        for i in range(self.dim):
            if self.grid[y][i] is not None:
                eligible[ self.grid[y][i] ] = False

    def check_local_box(self, x, y, eligible):
        for i in range(self.dim/3):
            for j in range(self.dim/3):
                if self.grid[y + i][x + j] is not None:
                    eligible[ self.grid[y + i][x + j] ] = False

    def fill_square(self, step, solution):
        x = self.moves[step]['x']
        y = self.moves[step]['y']

        self.grid[y][x] = solution[step]
        self.free_spaces -= 1

    def free_square(self, step, solution):
        x = self.moves[step]['x']
        y = self.moves[step]['y']
        self.grid[y][x] = None
        self.free_spaces += 1

    def __str__(self):
        board_str = ""
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                board_str += "---" * 10
                board_str += "\n"
            row_str = ""

            for j, space in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str += "|"
                row_str += (" {} ".format("-" if space is None else space))

            board_str += row_str
            board_str += "\n"
        return board_str
