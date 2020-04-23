import turtle as turtle
import random as random
import math

turtle.speed(0)
turtle.up()

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setProbability(self, probability):
        self.probability = probability


def square(side, point):
    x = point[0] - side / 2
    y = point[1] + side / 2
    turtle.goto(x, y)
    turtle.down()
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)
    turtle.up()
    turtle.goto(0, 0)

def writeProbability(terrariumSize,terrarium):
    turtle.goto(-terrariumSize, -terrariumSize)
    increment = terrariumSize/10
    for x in range(10):
        for y in range(10):
            turtle.write(terrarium[x][y], font=("Arial", 5, "normal"), align="center")
            turtle.goto(-terrariumSize/2 + x*increment, -terrariumSize/2 + y*increment)

def writeProbability(point):
    turtle.goto(point[0],point[1])
    turtle.write(terrarium[point[0]][point[1]], font=("Arial", 5, "normal"), align="center")

def terrarium(size):
    square(size,[0,0])
    terrarium = []
    for i in range(100):
        temp = []
        for j in range(100):
            p = Point(i,j)
            p.setProbability(1)
            temp.append(p)
        terrarium.append(temp)
    return terrarium

#terrarium = terrarium(int(input("Set terrarium size: ")))
terrarium = terrarium(700)

def chooseDirection(point):
    prob = []
    x = point.x-1
    y = point.y+1
    for i in range(terrarium[x][y].probability):
        prob.append(terrarium[x][y])

    x += 1
    for i in range(terrarium[x][y].probability):
        prob.append(terrarium[x][y])

    x += 1
    for i in range(terrarium[x][y].probability):
        prob.append(terrarium[x][y])

    y -= 1
    for i in range(terrarium[x][y].probability):
        prob.append(terrarium[x][y])

    y -= 1
    for i in range(terrarium[x][y].probability):
        prob.append(terrarium[x][y])

    x -= 1
    for i in range(terrarium[x][y].probability):
        prob.append(terrarium[x][y])

    x -= 1
    for i in range(terrarium[x][y].probability):
        prob.append(terrarium[x][y])

    y += 1
    for i in range(terrarium[x][y].probability):
        prob.append(terrarium[x][y])
    for element in prob:
        print("x = ",element.x," y = ",element.y)
    return random.choice(prob)

def gotoScaled(x,y):
    turtle.goto(x*7,y*7)

def ini():
    turtle.setworldcoordinates(-1,-1,700,700)
    pos = terrarium[50][50]
    turtle.down()
    move = True
    while move:
        dir = chooseDirection(pos)
        if 98 < pos.x < 0 or 98 < pos.y < 0:
            move = False
        else:
            turtle.goto(pos.x*7, pos.y*7)
            print("x = ", dir.x," y = ",dir.y)
            pos = dir
            #print("x = ", pos.x, " y = ", pos.y)


print (terrarium)
ini()


