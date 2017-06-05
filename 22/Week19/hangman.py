import turtle

MAX_ERRORS = 9

hangman_builder = turtle.Turtle()
hangman_builder.penup()
hangman_builder.goto(-100, -200)
hangman_builder.pendown()


def build_hangman(step):
    if step == 1:
        hangman_builder.left(90)
        hangman_builder.forward(300)
        
    elif step == 2:
        hangman_builder.right(90)
        hangman_builder.forward(100)
        
    elif step == 3:
        hangman_builder.right(90)
        hangman_builder.forward(50)
        
    elif step == 4:
        hangman_builder.penup()
        hangman_builder.right(90)
        hangman_builder.pendown()
        hangman_builder.circle(30)
        hangman_builder.penup()
        hangman_builder.left(90)
        hangman_builder.forward(60)
        
    elif step == 5:
        hangman_builder.pendown()
        hangman_builder.forward(120)
        
    elif step == 6:
        hangman_builder.left(45)
        hangman_builder.forward(60)
        
    elif step == 7:
        hangman_builder.back(60)
        hangman_builder.right(90)
        hangman_builder.forward(60)

    elif step == 8:
        hangman_builder.back(60)
        hangman_builder.left(-135)
        hangman_builder.forward(60)
        hangman_builder.right(-45)
        hangman_builder.forward(75)
        
    elif step == 9:
        hangman_builder.back(75)
        hangman_builder.left(-90)
        hangman_builder.forward(75)
        
    # Добавете до MAX_ERRORS стъпки
    else:
        print('You lost')


if __name__ == '__main__':
    for step in range(1, MAX_ERRORS + 1):
        build_hangman(step)

