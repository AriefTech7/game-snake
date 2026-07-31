from turtle import Turtle

UP=90
DOWN=270
RIGHT=0
LEFT=180


MOVE_DISTANCE = 20  # nilai pada konstan tidak akan bisa diubah
class Snake:
    def __init__(self):
        self.segments = []
        self.create_a_snake() # supaya function create_a_snake bisa langsung dijalankan ketika class Snake dipanggil
        self.head =self.segments[0]
        
    # function create_a_snake berfungsi untuk membuat kepala,badan dan ekor ular diawal game 
    def create_a_snake(self):
        a = 0
        # _ pada for loop berfungsi untuk memberitahu pembaca bahwa nilai iterasi tidak penting
        for _ in range(3):
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(a, 0)
            self.segments.append(snake)
            a -= 20

    def add_tail(self):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        self.segments.append(snake)
        x=self.segments[-1].xcor()
        y=self.segments[-1].ycor()
        self.segments[-1].goto(x,y)
            
    # function move berfungsi menggerakkan seluruh bagian tubuh ular
    def move(self): 
        for seg_num in range(len(self.segments)-1,0,-1):
            # xcor dan ycor berfungsi untuk mendapatkan koordinat
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_a_snake()
        self.head =self.segments[0]
           
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
            
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
        
    


    
    
    
        
    
    