import tkinter as tk

SQUARE_WIDTH = 100
SQUARE_HEIGHT = 100

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)  
        self.master.title("Code Combat")
        self.master.bind('<KeyPress>', self.move_hero)

        # Create a canvas on which to play the game
        self.board = tk.Canvas(self, height=500, width=500, bg="steelblue")

        # Creates all vertical lines at intevals of 100
        for i in range(0, 500, 100):
            self.board.create_line([(i, 0), (i, 500)], tag='grid_line')
            
        # Creates all horizontal lines at intevals of 100
        for i in range(0, 500, 100):
            self.board.create_line([(0, i), (500, i)], tag='grid_line')

        # Choose pics to represent players and traps
        self.spikes = tk.PhotoImage(file = 'images/spikes.png')
        self.wheelchair = tk.PhotoImage(file = 'images/wheelchair.png')
        self.start = tk.PhotoImage(file = 'images/start.png')
        self.finish = tk.PhotoImage(file = 'images/finish.png')
        self.hero = tk.PhotoImage(file = 'images/hero.png')
   
        # Draw the pictures on the canvas
        self.board.create_image(250,250,image=self.spikes, tags='spikes')
        self.board.create_image(450,50,image=self.wheelchair)
        self.board.create_image(50,50,image=self.start)
        self.board.create_image(450,450,image=self.finish)
        self.board.create_image(50,50,image=self.hero, tags='hero')
 
        # pack the board to enable display
        self.board.pack()
        self.pack()

    def move_hero(self, event):
        if event.keysym == "Up":
            self.board.move('hero', 0, -SQUARE_HEIGHT)          
        elif event.keysym == "Down":
            self.board.move('hero', 0, SQUARE_HEIGHT)
        elif event.keysym == "Left":
            self.board.move('hero', -SQUARE_WIDTH, 0)
        elif event.keysym == "Right":
            self.board.move('hero', SQUARE_WIDTH, 0)

        if self.board.coords('hero') == self.board.coords('spikes'):
            print('YOU LOST 50 HEALTH POINTS')       
        
def main():
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
    
if __name__ == '__main__':
    main()
