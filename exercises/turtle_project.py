"""TODO: A Traingle shaped House for my turtle friend with a nice neighborhood."""

__author__ = "730410860"

from turtle import Turtle, colormode, done


def draw_triangle(big_turtle: Turtle, x: float, y: float, size: float) -> None: 
    """Making a triangle that is the given size and will be pplanted at given coordinates of x and y."""
    big_turtle.penup()
    big_turtle.goto(x, y)
    big_turtle.setheading(90.0)
    big_turtle.pendown()
    i: int = 0
    while (i < 3):
        big_turtle.forward(size)
        big_turtle.right(150.0)


def draw_circle(big_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """This circle will be based on its radius and planed at x and y."""
    big_turtle.penup()
    big_turtle.goto(x, y - radius)
    big_turtle.setheading(0.0)
    big_turtle.pendown()
    big_turtle.circle(radius)


def draw_square(big_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square that will be filled with color at x and y."""
    big_turtle.penup()
    big_turtle.goto(x, y)
    big_turtle.setheading(0.0)
    big_turtle.pendown()
    big_turtle.begin_fill()
    i: int = 0
    while (i < 4):
        big_turtle.forward(width)
        big_turtle.right(90.0)
    big_turtle.end_fill()


def draw_tree(big_turtle: Turtle, length: float, height: int) -> None:
    """Recursive Tree branch with different size extension branches."""
    if height == 0:
        return
    else: 
        big_turtle.forward(length)
        big_turtle.left(45.0)
        draw_tree(big_turtle, length * 0.85, height - 1)
        big_turtle.right(45.0)
        draw_tree(big_turtle, length * 0.85, height - 1)
        big_turtle.left(45.0)
        big_turtle.backward(length)


def main() -> None:
    """The encryption point of my scene."""
    big_turtle: Turtle = Turtle()
    big_turtle.speed(0.0)
    big_turtle.color("blue", "yellow") 
    draw_square(big_turtle, -100, 100, 100)
    draw_square(big_turtle, 100, -100, 50)  
    big_turtle.color("blue")
    draw_circle(big_turtle, 100, 100, 50)
    big_turtle.color("blue", "green")
    draw_triangle(big_turtle, 0, -100, 100)
    done()


if __name__ == "__main__":
    colormode(255)
    main()
