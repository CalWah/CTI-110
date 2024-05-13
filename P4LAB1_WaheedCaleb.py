#Caleb Waheed
#3/26/2024
#P4LAB1
#Using loops and turtle to draw shapes

import turtle          
win = turtle.Screen()  
timmy = turtle.Turtle()

# add some display options
timmy.pensize(4)            # increase pensize (takes integer)
timmy.pencolor("purple")     # set pencolor (takes string)
timmy.shape("arrow")


#Use a for loop to draw the square
for side in range(4):
    timmy.forward(75)
    timmy.right(90)

#While loop to draw the triangle
counter = 0
while counter < 3:
    timmy.forward(75)
    timmy.left(120)
    counter += 1
