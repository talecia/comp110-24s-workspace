"""Create two similar functions, one that mutates and the other does not."""
__author__ = "730410860"

x: float
y: float

class Point:
    """Class represents a point on an (x,y) coordinate graph."""
    def __init__(self, x: float, y: float) -> None:
        """Changning value by multiplying x and y by a value."""
        self.x = x
        self.y = y

    def scale_by(self, factor: int) -> None:
        """Mutates a point by updating x and y values."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> "Point":
        """Instead of muttaing Point it creates a new Point."""
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
a: Point = Point(1.0, 2.0)
b: Point = a.scale(3.0)

print(type(1))
print(type(str(1)))