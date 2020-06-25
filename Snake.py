# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:28:19 2020

@author: vishal
"""


import turtle
import time
import random

delay = 0.20
score = 0
best = 0
segments = []


window = turtle.Screen()
window.title('Py Snake')
window.bgcolor("white")
window.setup(width = 600, height = 600)
window.tracer(0)

# Head
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0, 100)


# Food
head = turtle.Turtle()
head.speed(0)
head.color("black")
head.shape("square")
head.penup()
head.goto(0, 0)
head.direction = "stop"


pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.shape('square')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score : 0    Best : 0', align = 'center', font = ('Courier', 14, "bold"))

#segment = []

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x + 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x - 20)
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "d")
window.onkeypress(go_right, "a")       

# Main game loop
while True:
    window.update()
    
    
   # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()
        
        
# Reset score here
        score = 0
        
        delay = 0.1


        pen.clear()
        pen.write("Score :  {} Best : {}".format(score, best), align = "center", font = ("courier", 14, "bold"))
        
        
        
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("grey")
        body.penup()
        segments.append(body)
        
        score += 10
        
        delay -= 0.01
        
        if score > best:
            best = score
            
        pen.clear()
        pen.write("Score :  {} Best : {}".format(score, best), align = "center", font = ("courier", 14, "bold"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
        
    move()
    
    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()
            
            
# Reset score here
            score = 0
            
            delay = 0.1
            

            pen.clear()
            pen.write("Score :  {} Best : {}".format(score, best), align = "center", font = ("courier", 14, "bold"))
        
    
    
    time.sleep(delay)
    
window.mainloop()