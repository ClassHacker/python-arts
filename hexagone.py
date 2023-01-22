from turtle import Turtle,Screen,done
from random import randint

def hex(x:int):
    #p.fillcolor("grey")
    #p.begin_fill()
    for _ in range(6):
        p.fd(x)
        p.right(60)
    #p.end_fill()

def FillColor(pen:Turtle,col:str,x:int):
    pen.fillcolor(col)
    pen.begin_fill()
    for _ in range(2):
        pen.fd(x)
        pen.left(120)
        pen.fd(x)
        pen.left(60)
    pen.end_fill()

p = Turtle()
p.width(2)
p.speed(10)

s = Screen()
s.bgcolor("grey")
#s.delay(0)

col = ["Grey","black"]

x = 30
p.left(30)
for i in range(5):
    p.down()
    hex(x+x*i)
    p.up()
    p.back(15)
    p.left(90)
    p.fd(26)
    p.right(90)

p.right(60)
p.fd(180)

#p.down()
for i in range(5):
    FillColor(p,col[i%2],150-30*i)
p.right(180)
col = ["black","grey"]
for i in range(5):
    FillColor(p,col[i%2],150-30*i)

p.width(1)
p.down()
p.right(120)
p.fd(150)
p.fd(-300)
p.ht()
done()
