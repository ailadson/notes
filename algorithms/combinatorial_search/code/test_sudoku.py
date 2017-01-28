from backtrack_sudoku import sudoku_solver
from sudoku_board import Board

print "~~~~~Simple Sudoku~~~~~~"
simple = [
    [None,None,None,  None,8,None, None,None,None],
    [None,None,None,  5,None,9,     None,None,None],
    [None,9,None,     7,None,3,    None,8,None],

    [None,None,4,  9,None,6,       2,None,None],
    [None,None,2,  4,None,1,       5,None,None],
    [1,None,None,  None,None,None, None,None,7],

    [None,6,8,        None,None,None,  1,7,None],
    [None,None,None, 6,None,5,        None,None,None,],
    [None,None,9,    None,3,None,     4,6,None],
]

sudoku_solver(simple)

print "=*" * 30
print "*=" * 30
print "=*" * 30

print "~~~~~Easy Sudoku~~~~~~"
easy = [
    [None,1,None,    3,None,None, None,8,None],
    [None,None,None, 9,4,None,    None,2,None],
    [None,None,4,    None,8,7,    None,None,None],

    [None,4,None,  None,None,None,   2,3,None],
    [None,None,8,  None,None,None,   4,None,None],
    [None,3,2,     None,None,None,   None,9,None],

    [None,None,None, 7,9,None,    8,None,None],
    [None,2,None,    1,5,4,       None,None,None],
    [None,6,None,    None,None,3, None,1,None],
]

sudoku_solver(easy)

print "=*" * 30
print "*=" * 30
print "=*" * 30

print "~~~~~Medium Sudoku~~~~~~"
medium = [
    [None,None,None, 8,2,None,     5,None,None],
    [2,None,None,    None,None,6,   None,None,None],
    [7,None,None,    None,3,None,  None,None,1],

    [None,6,4,       7,None,None,   None,None,None],
    [None,7,None,    None,4,None,   None,6,None],
    [None,None,None, None,None,1,   4,5,None],

    [4,None,None,    None,1,None,  None,None,8],
    [8,None,None,    2,None,None,  None,None,9],
    [None,None,3,    None,None,4,  None,None,None],
]

sudoku_solver(medium)

print "=*" * 30
print "*=" * 30
print "=*" * 30

print "~~~~~Hard Sudoku~~~~~~"
hard = [
    [None,None,None, None,9,None,     None,None,None],
    [None,None,8,    None,None,None,  None,3,7],
    [6,7,None,       4,None,None,     8,None,None],

    [None,3,None,    None,8,2,         4,6,None],
    [None,None,None, None,None,None,   None,None,None],
    [None,9,2,       1,4,None,         None,7,None],

    [None,None,6,    None,None,9,    None,8,4],
    [5,1,None,       None,None,None, 6,None,None],
    [None,None,None, None,5,None,    None,None,None],
]

sudoku_solver(hard)

print "=*" * 30
print "*=" * 30
print "=*" * 30

print "~~~~~AGM Sudoku~~~~~~"
AGM = [
    [None,None,None,  None,None,None,  None,1,2],
    [None,None,None,  None,3,5,        None,None,None],
    [None,None,None,  6,None,None,     None,7,None],

    [7,None,None,     None,None,None,  3,None,None],
    [None,None,None,  4,None,None,     8,None,None],
    [1,None,None,     None,None,None,  None,None,None],

    [None,None,None,  1,2,None,None, None,None],
    [None,8,None,     None,None,None,  None,4,None],
    [None,5,None,     None,None,None,  6,None,None]
]

sudoku_solver(AGM)
