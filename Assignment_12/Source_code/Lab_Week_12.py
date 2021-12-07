########################################################################
##
## CS 101 Lab
## Program Week 12
## Name Bishop Lohman
## Email brlcxc@umsystem.edu
##
## Algorithm:
## Error Handling:
## Other Comments:
##
########################################################################
import turtle

class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
        
    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x, y, width, height, color):
        Point.__init__(self, x, y, color)
        self.width = width
        self.height = height

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class BoxFilled(Box):
    def __init__(self, x, y, width, height, color, fillcolor):
        Box.__init__(self, x, y, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x, y, radius, color):
        Point.__init__(self, x, y, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x, y, radius, color, fillcolor):
        Circle.__init__(self, x, y, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()

def main():
    p = Point(-100, 100, "blue")
    p.draw()
    b = Box(-100, 100, 50, 20, 'blue')
    b.draw()
    b = BoxFilled(1, 2, 100, 200, "red", "Blue")
    b.draw()
    c = Circle(100, 100, 30, 'red')
    c.draw()
    c = CircleFilled(150, 150, 50, 'red', 'blue')
    c.draw()

if __name__ == "__main__":
    main()