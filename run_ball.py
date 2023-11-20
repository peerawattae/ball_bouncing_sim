
from ball import Ball
import turtle

num_balls = int(input("Enter number of ball to sim: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
turtle.colormode(255)

canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 20

balls = [Ball(canvas_width, canvas_height, ball_radius) for _ in range(num_balls)]

while True:
        turtle.clear()

        for ball in balls:
            ball.move(canvas_width, canvas_height)
            ball.draw()

        turtle.update()

canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
color_list = []
xpos = []
ypos = []
vx = []
vy = []
ball_color = []
ball.initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls)
while (True):
    turtle.clear()
    for i in range(num_balls):
        ball.draw_circle(ball_color[i], ball_radius, xpos[i], ypos[i])
        ball.move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
