#! /usr/bin/env python3
import math


class Point:
    # Origin definition
    x_origin, y_origin = (0, 0)

    def __init__(self, x=x_origin, y=y_origin):
        """ Initialize to origin """
        self.x = x
        self.y = y

    @property
    def location(self):
        """ Return a tuple of position """
        return self.x, self.y

    def move(self, x_new, y_new):
        """ Update the x, y position. """
        self.x = x_new
        self.y = y_new

    def distance(self, other_position):
        """ returns distance measurement. """
        return math.sqrt(
            (self.x - other_position.x)**2 +
            (self.y - other_position.y)**2
        )

    def __repr__(self):
        return '{0}, {1}'.format(self.X, self.Y)

    @property
    def X(self):
        return self.x

    @property
    def Y(self):
        return self.y

    def __eq__(self, other):
        """ Compare two points """
        if self.X == other.X and self.Y == other.Y:
            return True
        return False

def main():
    # Create a point p1
    # with corodiates at 5, 10
    p1 = Point(x=5, y=10)

    # ... p2 with coordinates 13, 15
    p2 = Point(x=13, y=15)

    # .... p3 with default coordiantes
    # which should be 0,0
    p3 = Point()

    # validate if its true, is it at origin
    assert p3 == Point(0,0)

    # compare tuples
    # (use a property instead of a method)
    # Note: a property is represented as a field, but is a method

    assert p3.location == (0, 0)

    # move p1 to a new location
    p1.move(3,5)

    # verify that p1 has been moved
    assert p1.location == (3, 5)

    # What is the distance between two points?
    print(p1)
    print(p2)
    print(p1.distance(p2))


if __name__ == '__main__':
    main()