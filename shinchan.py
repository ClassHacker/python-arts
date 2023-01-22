from turtle import Turtle,Screen,done

p = Turtle()
p.width(2)
p.up()
s = Screen()
s.bgcolor("pink")
s.delay(0)

def hands():
    pen = Turtle()
    pen.goto(133,120)
    pen.width(2)
    pen.fillcolor("#ecbcb4")
    pen.begin_fill()
    pen.left(45)
    pen.fd(5)
    pen.right(90)
    pen.circle(5,90)
    pen.fd(10)
    pen.right(30)

    pen.circle(4,-90)
    pen.circle(3,90)
    pen.circle(6,90)
    pen.circle(3,90)

    pen.left(-90)
    pen.circle(3,90)
    pen.circle(6,90)
    pen.circle(3,90)
    pen.circle(6,90)

    pen.circle(4,90)
    pen.right(145)

    pen.circle(60,20)
    pen.circle(2,150)
    pen.circle(50,20)

    pen.right(160)
    pen.circle(50,20)
    pen.circle(2,150)
    pen.circle(70,20)


    pen.end_fill()
    pen.ht()

def pants():
    r = Turtle()
    r.width(2)
    r.up()
    r.goto(63,-22)
    r.down()
    r.fillcolor("yellow")
    r.begin_fill()
    r.right(85)
    r.fd(60)
    r.right(90)
    r.fd(65)
    r.right(80)
    r.fd(15)
    r.left(60)
    r.fd(15)
    r.back(13)
    r.left(90)
    r.fd(15)
    r.right(80)
    r.fd(65)
    r.right(95)
    r.fd(64.5)
    r.ht()
    r.end_fill()

def legs():
    #left leg
    pen = Turtle()
    pen.ht()
    pen.width(2)
    pen.goto(38,-140)

    #pen for shoes
    pen1 = pen.clone()
    pen1.fillcolor("yellow")
    pen1.begin_fill()
    pen1.right(130)
    pen1.fd(15)
    pen1.right(-120)
    pen1.fd(50)
    pen1.left(150)
    pen1.fd(25)
    pen1.right(50)
    pen1.fd(10)
    pen1.circle(3.5,180)
    pen1.fd(5)
    pen1.ht()
    pen1.end_fill()
    #done()

    pen.fillcolor("white")
    pen.begin_fill()
    pen.fd(13)
    pen.left(92)

    #pen for socks
    pen2 = pen.clone()
    pen2.fd(20)
    pen2.right(75)
    pen2.circle(60,-17)
    pen2.end_fill()
    pen2.ht()

    pen.fd(58)
    pen.ht()

    #right leg
    pen = Turtle()
    pen.ht()
    pen.width(2)
    pen.goto(-38,-140)

    #pen for shoes
    pen1 = pen.clone()
    pen1.fillcolor("yellow")
    pen1.begin_fill()
    pen1.right(130-80)
    pen1.fd(15)
    pen1.right(120)
    pen1.fd(50)
    pen1.left(-150)
    pen1.fd(25)
    pen1.right(-50)
    pen1.fd(10)
    pen1.circle(-3.5,180)
    pen1.fd(5)
    pen1.ht()
    pen1.end_fill()
    #done()

    #pen for socks
    pen2 = pen.clone()

    pen.fd(-13)
    pen.left(92)
    pen.fd(58)
    pen.ht()

    pen2.fillcolor("white")
    pen2.begin_fill()
    pen2.fd(-13)
    pen2.left(92)
    pen2.fd(20)
    pen2.right(-75)
    pen2.circle(60,-17)
    pen2.end_fill()
    pen2.ht()


def eye(p):
    p.down()
    p.dot(35)
    p.fd(2)
    p.color("White")
    p.dot(15)
    p.color("black")
    p.up()

def eyebrows():
    pen = Turtle()
    pen.color("#222222")
    pen.up()
    pen.goto(-30,210)
    pen.width(15)
    pen.down()
    pen.right(120)
    pen.circle(150,-10)
    pen.right(90)
    pen.circle(150,-10)
    pen.up()
    pen.goto(30,205)
    pen.down()
    pen.left(105)
    pen.circle(150,-10)
    pen.right(90)
    pen.circle(150,-15)
    pen.ht()

def shinchan(posx,posy):
    hands()
    #done()
    #drawing lower body
    legs()
    pants()

    p.begin_poly()
    p.goto(-10,180)
    #eyes
    eye(p)
    p.right(10)
    p.forward(60)
    eye(p)
    #done()

    p.right(5)
    p.fd(40)
    p.left(105)
    p.down()
    p.circle(60,45)
    p.circle(120,45)
    p.circle(30,90)

    #save cordinates for future use
    x = p.get_poly()[-1][0]
    y = p.get_poly()[-1][1]

    p.fd(30)
    p.right(90)
    p.circle(40,180)
    p.circle(40,-18)
    p.right(90)
    

    #elipse-mouth
    p.fillcolor("#aa0000")
    p.begin_fill()
    p.circle(12,90)
    p.circle(20,99)
    p.circle(12,90)
    p.circle(20,99)
    p.end_fill()
    #done()

    #new pen for chest
    q = p.clone()
    q.fillcolor("red")
    q.begin_fill()
    q.circle(12,90)
    q.circle(20,45)
    q.right(45)
    q.circle(240,35)
    q.right(10)
    q.fd(15)
    q.circle(-10,-210)
    q.circle(-500,12)
    q.circle(20,45)
    q.fd(50)
    q.right(90)
    q.fd(115)
    q.circle(-15,105)
    q.fd(75)
    q.back(15)
    q.left(50)
    q.fd(100)
    q.right(30)
    q.fd(7)
    q.right(90)
    q.circle(10,90)
    q.right(120)
    q.fd(21)
    q.right(86)
    q.circle(40,95)
    q.ht()

    q.end_fill()
    #end body

    p.circle(12,90)
    p.circle(20,45)
    p.right(45)
    p.circle(240,35)

    #hair
    p.left(50)
    p.circle(30,60)
    p.fillcolor("black")
    p.begin_fill()
    p.circle(10,90)
    p.fd(20)
    p.right(145)
    p.fd(40)
    p.circle(20,45)
    p.circle(120,40)
    p.circle(30,90)

    p.goto(x,y)
    p.left(5)
    p.circle(30,-90)
    p.circle(120,-45)
    p.circle(60,-45)
    p.end_fill()
    p.up()

    p.goto(x+10,y-15)
    p.down()
    p.circle(-17,190)
    p.up()
    p.left(10)
    p.goto(x+68,y-25)
    p.down()
    p.circle(18,-180)
    p.up()

    #eyebrows
    eyebrows()
    #done()


shinchan(0,0)
#s.bgcolor("#ecbcb4")
p.ht()
done()
