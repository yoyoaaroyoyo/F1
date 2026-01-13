import turtle
import random

   #setup
red = turtle.Turtle()
blue = turtle.Turtle()
green = turtle.Turtle()
yellow = turtle.Turtle()
finish = 100
start_x = -50

   #screen
s = turtle.Screen()
s.window_width()
s.window_height()
s.bgcolor("white")
s.title("F1 race")
turtle.tracer()  #to disable auto updates

    #red
red.color("red")
red.penup()
red.goto(start_x,50)     #set position
red.pendown()

    #blue
blue.color("blue")
blue.penup()
blue.goto(start_x,-50)   #set position
blue.pendown()

    #green
green.color("green")
green.penup()
green.goto(start_x,20)     #set position
green.pendown()

    #yellow
yellow.color("yellow")
yellow.penup()
yellow.goto(start_x,-20)     #set position
yellow.pendown()


def f1():
    
    x = True

    while x == True: 
              #checking if they have reached finish line
        red.forward(random.randint(0,1))
        blue.forward(random.randint(0,1))
        green.forward(random.randint(0,1))
        yellow.forward(random.randint(0,1))
        #These are needed for smooth animation
        if red.xcor() > finish or blue.xcor() > finish or green.xcor() > finish or yellow.xcor() > finish:
          x = False 
        else:
          x = True

    turtle.update()

    if red.xcor() >= finish:
            print("Red wins!")
    if blue.xcor() >= finish:
            print(" Blue wins!")
    if green.xcor() >= finish:
            print("Green wins!")
    if yellow.xcor() >= finish:
            print("Yellow wins!")


f1()

turtle.done()