import turtle as t
import random as rd

t.bgcolor('skyblue')

cp = t.Turtle()
cp.shape('square')
cp.color('orange')
cp.speed(0)
cp.penup()
cp.hideturtle()

lf = t.Turtle()
lf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('lf',lf_shape)
lf.shape('lf')
lf.color('green')
lf.penup()
lf.hideturtle()
lf.speed()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align='center',font=('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = cp.pos()
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside

def game_over():
    cp.color('red')
    lf.color('skyblue')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))

def place_lf():
    lf.hideturtle()
    lf.setx(rd.randint(-200,200))
    lf.sety(rd.randint(-200,200))
    lf.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    cp_speed = 2
    cp_length = 3
    cp.shapesize(1,cp_length,1)
    cp.showturtle()
    display_score(score)
    place_lf()

    while True:
        cp.forward(cp_speed)
        if cp.distance(lf)<20:
            place_lf()
            cp_length = cp_length + 1
            cp.shapesize(1,cp_length,1)
            cp_speed = cp_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if cp.heading() == 0 or cp.heading() == 180:
        cp.setheading(90)

def move_down():
    if cp.heading() == 0 or cp.heading() == 180:
        cp.setheading(270)

def move_left():
    if cp.heading() == 90 or cp.heading() == 270:
        cp.setheading(180)

def move_right():
    if cp.heading() == 90 or cp.heading() == 270:
        cp.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
