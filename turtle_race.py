from turtle import Turtle
from random import randint

laura = Turtle()
robbin = Turtle()
john = Turtle()
james = Turtle()

laura.color('orange')
laura.shape('turtle')
laura.penup()
laura.goto(-160,100)
laura.pendown()

robbin.color('brown')
robbin.shape('turtle')
robbin.penup()
robbin.goto(-160,75)
robbin.pendown()

john.color('blue')
john.shape('turtle')
john.penup()
john.goto(-160,50)
john.pendown()

james.color('green')
james.shape('turtle')
james.penup()
james.goto(-160,25)
james.pendown()

for movement in range(100):
    laura.forward(randint(1,5))
    robbin.forward(randint(1,5))
    john.forward(randint(1,5))
    james.forward(randint(1,5))
