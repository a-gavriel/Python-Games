from tkinter import *
from random import randrange

Width = 600
Height = 400
Scale = 20

def place_food(tail):
    x1,y1,_,_ = canvas.coords(player)    
    cx1,cy1,_,_ = canvas.coords(food)
    eq = True
    while eq:
        fx1 = randrange(Width//Scale)*Scale
        fy1 = randrange(Height//Scale)*Scale
        eq = eq and (x1 != fx1) and (y1 != fy1)
        for i in range(len(tail)):
            tx1,ty1,_,_ = canvas.coords(tail[i])
            eq = eq and (tx1 != fx1) and (ty1 != fy1)
    canvas.move(food, fx1-cx1, fy1-cy1)

def change_dir(key):
    global Dir
    if key == "Left":
        Dir = key
    elif key == "Right":
        Dir = key 
    elif key == "Up":
        Dir = key
    elif key == "Down":
        Dir = key

def move_player(Alive, tail): 
    global Dir, Score
    x1,y1,x2,y2=(canvas.coords(player))    
    if Dir == "Left" and x1 > 0:        
        canvas.move(player, -1*Scale, 0)  
    elif Dir == "Left" and x1 == 0:        
        Alive = False
    elif Dir == "Right" and x2 < Width:
        canvas.move(player, Scale, 0)  
    elif Dir == "Right" and x2 == Width:  
        Alive = False
    elif Dir == "Up" and y1 > 0:
        canvas.move(player, 0, -1*Scale)        
    elif Dir == "Up" and y1 == 0:
        Alive = False
    elif Dir == "Down" and y2 < Height:
        canvas.move(player, 0, Scale)
    elif Dir == "Down" and y2 == Height:
        Alive = False

    cx1,cy1,cx2,cy2 = x1,y1,x2,y2
    for i in range(len(tail)):
        tx1,ty1,tx2,ty2 = canvas.coords(tail[i])
        canvas.move(tail[i], cx1-tx1, cy1-ty1)
        cx1,cy1 = tx1,ty1
        if x1 == cx1 and y1 == cy1:
            Alive = False
            
    check_collision(x1,y1,x2,y2, tail)
    if Alive == False:
        Alive = True
        print("Score was: ",Score)        
        newgame()
    main.after(100,move_player, Alive, tail)

def check_collision(x1,y1,x2,y2, tail):
    global Score
    sx1,sy1,_,_ =(canvas.coords(player))
    fx1,fy1,_,_ = canvas.coords(food)
    if fx1 == sx1 and fy1 == sy1:
        newRect = canvas.create_rectangle(x1,y1,x2,y2,fill="#88ff88")
        tail.append(newRect)
        Score += 1
        place_food(tail)

def game():
    global main, canvas, player, food, Dir, Score
    main = Tk()
    Dir = "Right"
    Score = 0
    main.geometry(str(Width)+"x"+str(Height)+"+200+200")
    main.resizable(width = False, height = False)
    main.focus_force()
    canvas = Canvas(main, width = Width, height = Height)
    canvas.pack()
    player = canvas.create_rectangle(Width//3, Height//2,Width//3 + Scale, Height//2 + Scale, fill = "green")
    tail = []
    Alive = True
    food = canvas.create_rectangle(100, 100,100 + Scale, 100 + Scale, fill = "red")
    place_food(tail)
    main.bind("<Key>", lambda event: change_dir(event.keysym))
    move_player(Alive, tail)
    main.mainloop()

def newgame():
    global main
    main.destroy()
    game()

game()