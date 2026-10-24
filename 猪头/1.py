import turtle

# 创建画笔
pig = turtle.Turtle()

# 设置速度
pig.speed(5)

# 画笔大小
pig.pensize(3)

# 画脸（圆）
pig.circle(100)


# 画眼睛
pig.penup()
pig.goto(-40, 120)
pig.pendown()
pig.fillcolor("black")
pig.begin_fill()
pig.circle(10)
pig.end_fill()

pig.penup()
pig.goto(40, 120)
pig.pendown()
pig.begin_fill()
pig.circle(10)
pig.end_fill()


# 画鼻子
pig.penup()
pig.goto(0, 60)
pig.pendown()

pig.fillcolor("pink")
pig.begin_fill()
pig.circle(35)
pig.end_fill()


# 鼻孔
pig.penup()
pig.goto(-12, 80)
pig.pendown()
pig.fillcolor("black")
pig.begin_fill()
pig.circle(5)
pig.end_fill()

pig.penup()
pig.goto(12, 80)
pig.pendown()
pig.begin_fill()
pig.circle(5)
pig.end_fill()


# 画耳朵
pig.penup()
pig.goto(-90, 150)
pig.pendown()
pig.fillcolor("pink")
pig.begin_fill()

for i in range(3):
    pig.forward(50)
    pig.left(120)

pig.end_fill()


pig.penup()
pig.goto(90, 150)
pig.pendown()
pig.begin_fill()

for i in range(3):
    pig.forward(50)
    pig.left(120)

pig.end_fill()


# 保持窗口
turtle.done()