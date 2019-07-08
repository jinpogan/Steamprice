import turtle
from random import randint as rand
import winsound
turtle.screensize()
turtle.setup(width = 1.0, height = 1.0)
turtle.colormode(255)
turtle.speed(0)
turtle.bgpic('./sadgaben.png')
#turtle.bgcolor(rand(0,255), rand(0,255), rand(0,255))
turtle.color(rand(0,255), rand(0,255), rand(0,255))
turtle.penup()
turtle.backward(550)
turtle.pendown()
turtle.write("GAME IS NOT ON SALE ANYMORE", font=("Arial", 70, "normal"))
turtle.penup()
turtle.forward(550)
turtle.pendown()
frequency = 1000  # Set Frequency To 2500 Hertz
duration = 20000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
