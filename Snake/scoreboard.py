from turtle import Turtle
ALIGMNET = "center"
FONT = ("Ariel", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("save.txt") as file:
            save = int(file.read())
        self.score = 0
        self.high_score = save
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.uptade_scoreboard()
        self.hideturtle()

    def uptade_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.uptade_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("save.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.uptade_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER ", align=ALIGMNET, font=FONT)
