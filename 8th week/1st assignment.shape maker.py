import turtle

t = turtle.Turtle()

color = input("\n\n\n\nplease enter a color: ")
sides = int(input("please enter the sides of the shape: "))

t.color(color)
for i in range(sides):
    t.forward(100)
    t.left(360.0/sides)

