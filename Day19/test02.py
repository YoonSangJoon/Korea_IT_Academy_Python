import turtle

turtle.shape("turtle")
for i in range(20, 100):
    turtle.forward(i)
    turtle.left(90)  # 90도 왼쪽으로 틀기
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)



turtle.exitonclick()