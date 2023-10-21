from turtle import Turtle, Screen;

pointer = Turtle();
screen = Screen();




def move_forward():
    pointer.forward(10);

def move_right():
    pointer.right(10);

def move_left():
    pointer.left(10);

def move_backwards():
    pointer.back(10);

def clear_screen():
    pointer.clear();
    pointer.pu();
    pointer.home();
    pointer.pd();


screen.listen();
screen.onkey(key="w", fun=move_forward);
screen.onkey(key="d", fun=move_right);
screen.onkey(key="a", fun=move_left);
screen.onkey(key="s", fun=move_backwards);
screen.onkey(key="c", fun=clear_screen);


screen.exitonclick()