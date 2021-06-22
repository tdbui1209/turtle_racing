from turtle import Turtle, Screen
import random


class Game:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.all_turtles = []
        self.turtle_colors = ['green', 'red', 'purple', 'yellow', 'blue']
        self.user_bet = self.screen.textinput(title='Đặt cược',
                                              prompt='Con rùa nào sẽ chiến thắng? [green, red, purple, yellow, blue]?')
        self.race_on = True
        self.screen.title('Turtle Racing 2021')

    def create_turtle(self):
        for i in range(5):
            turtle = Turtle(shape='turtle')
            turtle.penup()
            turtle.color(self.turtle_colors[i])
            turtle.goto(x=-350, y=200-100*i)
            self.all_turtles.append(turtle)

    def create_finish_line(self):
        finish_line = Turtle()
        finish_line.hideturtle()
        finish_line.penup()
        finish_line.goto(x=300, y=400)
        finish_line.pendown()
        finish_line.goto(x=300, y=-400)

    def start(self):
        while self.race_on:
            for turtle in self.all_turtles:
                turtle.forward(random.randint(0, 20))
                self.end()

    def end(self):
        for turtle in self.all_turtles:
            if turtle.xcor() >= 300:
                winning_turtle = turtle.pencolor()
                self.race_on = False
                if winning_turtle == self.user_bet:
                    print(f'Bạn đã thắng! Con rùa {winning_turtle} là con rùa thắng cuộc!')
                else:
                    print(f'Bạn đã thua! Con rùa {winning_turtle} là con rùa thắng cuộc!')

game = Game()
game.create_finish_line()
game.create_turtle()
game.start()
game.screen.exitonclick()