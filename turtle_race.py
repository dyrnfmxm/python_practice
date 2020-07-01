import turtle as t
t.speed(10)
t.rt(90)
n = 0
for i in range(-160,160,20):
    t.up()
    t.goto(i,100)
    t.down()
    t.write(n,align='center')
    n += 1
    t.fd(200)
t.lt(90)
t.up()
t.color('red','red')
t.goto(-180,60)
t.down()
t.fd(240)
t.stamp()

t.up()
t.color('blue','blue')
t.goto(-180,20)
t.down()
t.fd(230)
t.stamp()

t.up()
t.color('green','green')
t.goto(-180,-20)
t.down()
t.fd(230)
t.stamp()

t.up()
t.color('yellow','yellow')
t.goto(-180,-60)
t.down()
t.fd(220)
t.stamp()
