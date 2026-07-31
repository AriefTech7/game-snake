from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",20,"normal")
FONT_GAMEOVER = ("Arial",25,"bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("/home/guebanget/Documents/Python/Codingan Python Project/data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scorebord()
        self.hideturtle()
        

    def update_scorebord(self):
        self.clear()
        self.write(arg=f"Score = {self.score}  High Score = {self.high_score}",align=ALIGNMENT,font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER",align=ALIGNMENT,font=FONT_GAMEOVER)


    def increase_score(self):
        self.score+=1
        self.update_scorebord()
        
    def reset_score(self):
        if self.score > self.high_score:
            with open("/home/guebanget/Documents/Python/Codingan Python Project/data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scorebord()
        
    
       
