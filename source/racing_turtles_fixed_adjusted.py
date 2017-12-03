import turtle              # 1. import the modules
import random
import time
wn = turtle.Screen()       # 2. Create a screen
wn.setup(width = 420, height = 420, startx = 0, starty = 0)
lance = turtle.Turtle()    # 3. Create 4 turtles
andy = turtle.Turtle()
luis = turtle.Turtle()
michael = turtle.Turtle()
landscape = turtle.Turtle()

lance.ht()
andy.ht()
luis.ht()
michael.ht()

#Road setup
landscape.speed(3)
landscape.pensize(3)
landscape.ht()       #I dont want people see what I'm using to draw (my own turtle)
landscape.up()
landscape.setpos(-200,-200)
landscape.down()
landscape.color("White","DarkGray")

landscape.begin_fill()#landscape.fill(True)
for square in range(2):
    landscape.forward(400)
    landscape.left(90)
    landscape.forward(120)
    landscape.left(90)
landscape.end_fill()#landscape.fill(False)

landscape.up()
landscape.setpos(-200,-200)
for line in range(4):
    landscape.left(90)
    landscape.forward(30)
    landscape.right(90)
    for lot_of_paint in range(10):
        landscape.down()
        landscape.forward(20)
        landscape.up()
        landscape.forward(20)
    landscape.backward(400)
    
landscape.setpos(-200,-200)
landscape.pensize(5)
for line in range(2):
    landscape.down()
    for lot_of_paint in range(20):
        landscape.color("red")
        landscape.forward(10)
        landscape.color("white")
        landscape.forward(10)
    landscape.up()
    landscape.backward(400)  
    landscape.setpos(-200,-80)
    
landscape.setpos(180,-80)
landscape.pensize(8)
landscape.seth(270)
landscape.shape("square")

flag1 = 1                            
for line in range(4):
    landscape.down()
    if ((flag1 % 2) != 1):
        for lot_of_paint in range(10):
            landscape.color("black")
            landscape.forward(6)
            landscape.color("white")
            landscape.forward(6)
    else:
        for lot_of_paint in range(10):
            landscape.color("white")
            landscape.forward(6)
            landscape.color("black")
            landscape.forward(6)
    flag1 = flag1 + 1
    landscape.up()
    landscape.backward(120)  
    landscape.left(90)
    landscape.forward(6)
    landscape.right(90)
    
wn.bgcolor('skyblue')
    
landscape.speed(5)
landscape.up()
landscape.goto(-100,100)
landscape.color("yellow")
landscape.pensize(3)
landscape.speed(0)

for number_of_positions in range(1, 47, 1):    
    landscape.forward(60)         
    landscape.up()   
    landscape.forward(-60)
    landscape.down()
    landscape.right(8)

landscape.up()       
landscape.setpos(-90,-77)
landscape.pensize(1)
landscape.shape("arrow")  
landscape.color("black","green")

landscape.begin_fill()#landscape.fill(True)
landscape.seth(45)
landscape.down()
landscape.forward(100)
for degree in range(135):   #90 degrees + 45 degrees
    landscape.right(1)
    landscape.forward(1)
landscape.forward(30)
landscape.end_fill()#landscape.fill(False)

landscape.begin_fill()#landscape.fill(True)
landscape.seth(90)
landscape.forward(200)
for degree in range(180):   #90 degrees + 45 degrees
    landscape.right(1)
    landscape.forward(1)
landscape.forward(200)
landscape.end_fill()#landscape.fill(False)
landscape.penup()

#Getting the turtles ready (and nervous jaja)
lance.shape('turtle')
andy.shape('turtle')
luis.shape("turtle")
michael.shape("turtle")

lance.color('Olive')
andy.color('SaddleBrown')
luis.color("ForestGreen")
michael.color("DarkOliveGreen")

lance.st()
andy.st()
luis.st()
michael.st()

lance.up()
andy.up()                 
luis.up()
michael.up()

lance.goto(-190,-95)
andy.goto(-190,-125)
luis.setpos(-190,-155)
michael.setpos(-190,-185)

lance.speed(2)
andy.speed(2)
michael.speed(2)
luis.speed(2)

#Starting the race
landscape.shape("circle")
landscape.color("red")
landscape.setpos(-188,-60)
landscape.seth(0)

for countdown in range(3):
    landscape.st()
    time.sleep(0.5)
    landscape.ht()
    time.sleep(0.5)
   
landscape.color("LawnGreen")
landscape.st()
time.sleep(1.5)
landscape.ht()

lance_winner = 0
andy_winner = 0
luis_winner = 0
michael_winner = 0

winners_flag = 0
for i in range(50):
    if (lance.xcor()<200):
        lance.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (lance_winner == 0):
                print("Lance is the first place")
                lance_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (lance_winner == 0):
                print("Lance is the second place")
                lance_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (lance_winner == 0):
                print("Lance is the third place")
                lance_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (lance_winner == 0):
                print("Lance is the fourth place")
                lance_winner = 1
                winners_flag = 4
    
    if (andy.xcor()<200):
        andy.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (andy_winner == 0):
                print("Andy is the first place")
                andy_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (andy_winner == 0):
                print("Andy is the second place")
                andy_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (andy_winner == 0):
                print("Andy is the third place")
                andy_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (andy_winner == 0):
                print("Andy is the fourth place")
                andy_winner = 1
                winners_flag = 4       
        
    if (luis.xcor()<200):
        luis.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (luis_winner == 0):
                print("Luis is the first place")
                luis_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (luis_winner == 0):
                print("Luis is the second place")
                luis_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (luis_winner == 0):
                print("Luis is the third place")
                luis_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (luis_winner == 0):
                print("Luis is the fourth place")
                luis_winner = 1
                winners_flag = 4  
     
    if (michael.xcor()<200):
        michael.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (michael_winner == 0):
                print("Michael is the first place")
                michael_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (michael_winner == 0):
                print("Michael is the second place")
                michael_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (michael_winner == 0):
                print("Michael is the third place")
                michael_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (michael_winner == 0):
                print("Michael is the fourth place")
                michael_winner = 1
                winners_flag = 4  
wn.exitonclick()
