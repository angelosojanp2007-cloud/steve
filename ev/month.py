# x=int(input("Enter a month number"))
# if x==1:
#     print("January")
# elif x==2:
#     print("february")
# elif x==3:
#     print("March")
# elif x==4:
#     print("April")
# elif x==5:
#     print("May")
# elif x==6:
#     print("June")
# elif x==7:
#     print("July")
# elif x==8:
#     print("August")
# elif x==9:
#     print("Srptember")
# elif x==10:11
#     print("October")
# elif x==11:
#     print("November")
# elif x== 12:
#     print("December")
# else :
# print('invalid month')


import turtle
wn = turtle.Screen()
wn.title("Heart shape with text")
wn.bgcolor("white")

pen = turtle.Turtle()
pen.color("red")
pen.pensize(10)
pen.speed(1)

def draw_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90,200)
    pen.left(120)
    pen.circle(-90,200)
    pen.forward(180)
    pen.end_fill()

def write_text():
    pen.up()
    pen,setpos(0,50)
    pen.down()
    pen.color("blue")
    pen.write("HI",align="center",font=("Arial",29,"italic","bold"))


draw_heart()


write_text()


pen.hideturtle()
wn.mainloop()
        



