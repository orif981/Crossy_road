from turtle import Turtle

FONT = ["Courier", 8, "normal"]
random1 = 8


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.setpos(0, 280)
        self.level = 1
        self.write(f"Level: {self.level}", False, "center", FONT)

    def rewrite(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        FONT[1] = 30
        gameover = Turtle()
        gameover.pu()
        gameover.hideturtle()
        gameover.write(f"GAME OVER", False, "center", FONT)

    def won(self):
        FONT[1] = 30
        win = Turtle()
        win.pu()
        win.hideturtle()
        win.write(f"You have beaten the game!!", False, "center", FONT)
