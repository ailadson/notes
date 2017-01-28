def area_of_tri(a,b,c):
    ax, ay = a.x, a.y
    bx, by = b.x, b.y
    cx, cy = c.x, c.y
    return (ax*by - ay*bx + ay*cx - ax*cy + bx*cy - by*cx)/2.0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    print area_of_tri(Point(0,0), Point(0,5), Point(5,0))
