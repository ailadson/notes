from collections import defaultdict
from Queue import *

def searchMaze(maze, s, e):
    pred = {}
    edges = [[1,0], [0, 1], [-1,0], [0, -1]]
    q = Queue()
    q.put(s)

    while q.empty() is not True:
        coord = q.get()
        coord_id = getIDFromCoord(coord)
        for i, edge in enumerate(edges):
            row_i = coord[0] + edge[0]
            col_i = coord[1] + edge[1]
            space = [row_i, col_i]
            space_id = getIDFromCoord(space)

            if space_id not in pred and isAllowed(maze, row_i, col_i):
                pred[space_id] = coord_id

                if space == e:
                    q = Queue()
                    break;
                else:
                    q.put(space)

    if getIDFromCoord(e) not in pred:
        return []

    path = [e]

    while e != s:
        coordId = getIDFromCoord(e)
        print(coordId)
        e = getCoordFromID(pred.get(coordId))
        path.append(e)

    path.reverse()

    return path

def getIDFromCoord(coord):
    return "{0}{1}".format(coord[0], coord[1])

def getCoordFromID(id):
    return map(lambda i : int(i), list(id))

def isAllowed(maze, row, col):
    if 0 <= row < len(maze) and 0 <= col < len(maze[row]) and maze[row][col] is True:
        return True
    return False

a = searchMaze([
    [True, False, True, True, True],
    [True, True, True, False, False],
    [False, False, True, False, True],
    [True, True, True, False, True],
    [True, False, False, False, True],
    [True, True, True, True, True],
], [0, 0], [2, 4])

print (a)
