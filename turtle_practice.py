import turtle as t
"""t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
"""
for i in range(4):
    t.fd(100)
    t.lt(90)
t.up()
t.goto(200,0)
t.down()
#사각형
for i in range(2):
    t.fd(120)
    t.lt(120)
    t.fd(80)
    t.lt(60)
#평행사변형

t.up()
t.goto(200,-50)
t.down()
for i in range(5):
    t.fd(100)
    t.rt(360*2//5)
#별
    
t.up()
t.goto(-150,0)
t.down()
t.color('red','yellow')#선, 면 컬러 설정
t.begin_fill()        #채워진채로

while True:
    t.forward(100)
    t.left(170)
    x, y = t.pos()
    if int(x) == -150 and int(y) == 0:
        break
t.end_fill()
t.done()

t.up()
t.goto(0,-80)
t.down()
t.color('red','yellow')#선, 면 컬러 설정
t.begin_fill()        #채워진채로

while True:
    t.forward(100)
    t.left(170)
    if abs(t.pos()) < 1:
        print(t.pos())
        print(abs(t.pos()))
        break
t.end_fill()
t.done()
