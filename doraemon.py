from turtle import Turtle,Screen,done

p = Turtle()
s = Screen()
#s.delay(0)
p.width(3)
p.speed(10)
p.shape("turtle")

def Doraemon(xx=0,yy=0):
    p.begin_poly()
    #head
    col = "#3333ff"
    p.fillcolor(col)
    p.begin_fill()
    p.back(67.5)
    p.fd(135)
    p.left(35)
    p.circle(150,70)
    p.circle(130,150)
    p.circle(150,70)
    p.end_fill()
    p.left(35)
    #p.ht()
    #done() head

    #face
    p.fillcolor("white")
    p.begin_fill()
    p.fd(125)
    p.left(35)
    p.circle(130,60)
    p.circle(75,70)
    p.left(15)
    
    #right eye
    p.right(105)
    p.circle(45,45)
    p.circle(30,135)
    p.circle(45,45)
    p.circle(30,135)
    p.left(105)
    p.up()
    p.fd(45)
    p.dot(12)
    p.fd(14)
    #done re

    #left eye
    p.down()
    p.right(105)
    p.circle(45,45)
    p.circle(30,135)
    p.circle(45,45)
    p.circle(30,135)
    p.left(105)
    p.up()
    p.fd(14)
    p.dot(12)
    p.fd(45)
    p.left(15)
    #done() le

    p.down()
    p.circle(75,70)
    p.circle(130,60)
    p.end_fill()

    #nose
    p.up()
    p.goto(0,160)
    p.dot(25,"red")
    p.goto(-2,162)
    p.dot(7,"white")
    #done() nose

    #smile
    p.goto(0,145)
    p.down()
    p.goto(0,50)
    p.left(35)
    p.fd(10)
    p.circle(120,45)
    p.circle(120,-45)
    p.back(20)
    p.circle(120,-45)
    #done() smile

    #mustache
    p.width(2)
    p.up()
    p.goto(35,135)
    for _ in range(2):
        for _ in range(3):
            p.down()
            p.left(60)
            p.fd(50)
            p.fd(-50)
            p.up()
            p.right(105)
            p.fd(15)
            p.left(30)
        p.right(90)
        p.fd(45)
        p.right(45)
        p.fd(15)
    #done() mustache
    #done() face

    p.goto(-70,0)
    p.left(45)

    #belt
    p.down()
    p.fillcolor("red")
    p.begin_fill()
    for _ in range(2):
        p.fd(142)
        p.circle(-4,180)
    p.end_fill()
    p.up()
    #done()-belt
    
    #another pen for color filling
    t = Turtle()
    t.speed(0)
    t.width(3)
    t.shape("turtle")
    t.up()

    #body
    p.fillcolor(col)
    p.begin_fill()
    p.down()
    p.width(3)
    p.circle(-4,-120)
    p.left(90)

    #left-hand
    p.circle(100,45)
    p.right(60)
    t.goto(p.get_poly()[-1][0],p.get_poly()[-1][1])
    t.down()
    t.right(165)
    t.fillcolor("white")
    t.begin_fill()
    t.circle(20)
    t.up()
    t.end_fill()
    p.circle(20,-90)
    p.right(90)
    p.circle(100,12)
    p.right(117)
    #done()

    #legs
    p.back(25)
    p.fd(120)
    #foots
    t.goto(p.get_poly()[-1][0],p.get_poly()[-1][1])
    t.down()
    #t.begin_fill()
    t.right(15)
    t.circle(30,90)
    t.circle(15,90)
    t.fd(92)
    t.left(90)
    t.fd(60)
    t.left(90)
    t.fd(12)
    t.back(24)
    t.fd(12)
    t.left(90)
    t.fd(60)
    t.left(90)
    t.fd(92)
    t.circle(15,90)
    t.circle(30,90)
    #t.end_fill()
    t.up()
    #done-foots

    p.dot()
    p.left(60)
    p.circle(80,15)
    p.left(15)
    p.fd(120)
    p.left(15)
    p.circle(80,15)

    p.left(60)
    p.fd(120)
    p.back(25)
    p.right(100)
    p.circle(-100,10)
    p.right(90)
    #done-legs

    #right-hand
    p.circle(20,-90)
    t.goto(p.get_poly()[-1][0],p.get_poly()[-1][1])
    t.right(20)
    t.begin_fill()
    t.down(); t.circle(20); t.up()
    t.end_fill()
    p.right(55)
    p.circle(100,45)
    p.end_fill()
    p.up()
    #done()-right-hand

    #pocket
    t.goto(-49,-8)
    t.left(65)
    t.begin_fill()
    t.down()
    t.circle(75,270)
    t.up()
    t.end_fill()
    t.goto(-43,-8)

    t.goto(-43,-50)
    t.left(120)
    t.down()
    t.circle(47,210)
    t.goto(-43,-50)
    t.up()
    t.ht()
    #done() - pocket

    #belt
    p.goto(-70,0)
    p.right(150)
    p.down()
    p.fillcolor("red")
    p.begin_fill()
    for i in range(2):
        p.fd(142)
        p.circle(-4,180)
    p.end_fill()
    p.up()
    #done()-belt

    #bell
    p.goto(0,-20)
    p.down()
    p.dot(33)
    p.dot(30,"yellow")
    p.goto(0,-24)
    p.dot(10)
    p.goto(0,-35)
    p.up()
    p.ht()
    #done()

    #name
    t.goto(-120,-275)
    t.color("blue")
    t.write("Doraemon",font=("Comic Sans MS",40,"bold"))
    p.goto(0,-290)
    p.write("-ClassHacker",font=("vardana",15,"italic"))


p.end_poly()
#Doraemon()
s.onclick(Doraemon)
s.mainloop()
#done()
