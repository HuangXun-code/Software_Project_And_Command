try:
    import Tkinter as tkinter # python 2
except ImportError:
    import tkinter

import Model
import RepeatableTimer

class GUI(object):
    
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('500x440')
        
        self.canvas = tkinter.Canvas(self.root, bg='white', width=360, height=360)
        self.canvas.place(x=20, y=20)
        self.round_label = tkinter.Label(self.root, text='round:0')
        self.round_label.place(x=20, y=396)
        self.start_button = tkinter.Button(self.root, text='start', width=8, command=self.start_button_onclick)
        self.start_button.place(x=316, y=396)
        
        self.model = Model.Model()
        
        tkinter.mainloop()        
    
    def on_timer(self):
        self.model.update()
        self.drawMap(self.model.map, self.model.num_of_rows, self.model.num_of_cols)
        self.round_label['text'] = 'round:%r' % self.model.round
    
    def start_button_onclick(self):
        self.start_button['state'] = 'disabled'
        timer = RepeatableTimer.RepeatableTimer(0.3, self.on_timer)
        timer.start()
    
    def drawMap(self, map, num_of_rows, num_of_cols):
        width = float(self.canvas['width'])
        height = float(self.canvas['height'])
        unit_width = width / num_of_cols
        unit_height = height / num_of_rows
        self.canvas.create_rectangle(0, 0, width, height, fill='white', outline='white')
        for i in range(num_of_rows):
            for j in range(num_of_cols):
                if map[i][j] == 1:
                    self.canvas.create_rectangle(j*unit_width,
                                                 i*unit_height,
                                                 j*unit_width+unit_width-1,
                                                 i*unit_height+unit_height-1,
                                                 fill='black',
                                                 outline='white')                    
