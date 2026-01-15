# import turtle
# timmy = turtle.Turtle()

# Rather than the above, import the class:

from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.fillcolor("chartreuse")
timmy.fd(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()