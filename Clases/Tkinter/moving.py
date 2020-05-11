import tkinter as tk

class Game(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.can = tk.Canvas(self, width=200, height=200)
        self.can.pack(fill="both", expand=True)
        self.player = self.can.create_oval(50,50,70,70, fill="red")
        self.bind("<Key>", self.move_player)

    def move_player(self, event):
        key = event.keysym
        if key == "Left":
            self.can.move(self.player, -20, 0)        
        elif key == "Right":
            self.can.move(self.player, 20, 0)    
        elif key == "Up":
            self.can.move(self.player, 0, -20)        
        elif key == "Down":
            self.can.move(self.player, 0, 20) 

if __name__ == '__main__':
    game = Game()
    game.mainloop()