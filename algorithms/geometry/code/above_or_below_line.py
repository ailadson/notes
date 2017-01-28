from area_of_tri import *

def above_or_below_line(a, b, c):
    return 1 if area_of_tri(a, b, c) > 0 else -1

if __name__ == '__main__':
    print above_or_below_line(Point(0,0), Point(0,3), Point(-2,5))
