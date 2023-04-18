import turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.speed(0)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.width(50)

for color in colors:
    turtle.color(color)
    turtle.forward(600/len(colors))
    turtle.right(180-(180*(len(colors)-2)/(2*len(colors))))
    
turtle.hideturtle()
turtle.done()
