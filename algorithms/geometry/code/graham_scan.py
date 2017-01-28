import math
from above_or_below_line import *

def convex_hull(points):
    select_lowest_point(points)
    points = sort_points(points)
    hull = []
    print points
    hull.append(points[0])
    hull.append(points[1])
    hull.append(points[2])
    h_idx = 2

    # print points
    for i in range(3, len(points)):
        while above_or_below_line(hull[h_idx - 1], hull[h_idx], points[i]) > 0:
            hull.pop()
            h_idx -= 1
            if h_idx <= 1:
                break
        hull.append(points[i])
        h_idx += 1

    return hull

def sort_points(points):
    center = points[0]
    # print center
    def sort_cmp(point1, point2):
        if point1 is center:
            return -1
        if point2 is center:
            return 1
        return cmp(polar_angle(center, point2), polar_angle(center, point1))

    return sorted(points, sort_cmp)

def select_lowest_point(points):
    lowest_y = float('inf')
    lowest_x = float('inf')
    lowest_idx = None

    for i, point in enumerate(points):
        if point.y < lowest_y or (lowest_y == point.y and point.x < lowest_x) :
            lowest_y = point.y
            lowest_x = point.x
            lowest_idx = i

    points[0], points[lowest_idx] = points[lowest_idx], points[0]

def polar_angle(p1, p2):
    delta_x = p2.x - p1.x
    delta_y = p2.y - p1.y
    return math.atan2(delta_y, delta_x)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{},{}".format(self.x, self.y)

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    p = [Point(1,1), Point(0,0), Point(0,1), Point(0.5,0.75), Point(1,0)]
    print convex_hull(p)
