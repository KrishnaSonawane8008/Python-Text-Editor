from tkinter import *
from tkinter import ttk

class ScrollableFrame(ttk.Frame):

    def __init__(self, parent, Height=0, Width=0, Bg="white"):
        ttk.Frame.__init__(self, parent)

        self.parent=parent
        self.Height=Height
        self.Width=Width
        self.Bg=Bg

        self.main_frame=Frame(self, bg=self.Bg, width=self.Width, height=self.Height)
        self.main_frame.grid(row=0, column=0)
        self.main_frame.grid_propagate(False)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.my_canvas=Canvas(self.main_frame, bg=self.Bg)
        self.my_canvas.grid(row=0, column=0, sticky="nsew")

        self.ver_scrollbar=ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.ver_scrollbar.grid(row=0, column=1, sticky="ns", rowspan=2)

        self.hor_scrollbar=ttk.Scrollbar(self.main_frame, orient=HORIZONTAL, command=self.my_canvas.xview)
        self.hor_scrollbar.grid(row=1, column=0, sticky="ew")

        self.my_canvas.configure(yscrollcommand=self.ver_scrollbar.set, xscrollcommand=self.hor_scrollbar.set)

        self.frame=Frame(self.my_canvas, bg=self.Bg)
        self.frame.bind('<Configure>', self.update_scrollregion)
        self.my_canvas.create_window((0,0), window=self.frame, anchor="nw")

    def update_scrollregion(self, event):
        bbox = self.my_canvas.bbox("all")
        #print("update called")
        if bbox:
            self.my_canvas.config(scrollregion=bbox)
            self.my_canvas.configure(yscrollcommand=self.ver_scrollbar.set, xscrollcommand=self.hor_scrollbar.set)
        else:
            self.my_canvas.configure(yscrollcommand=None, xscrollcommand=None)

    def update_call(self):
        self.update_scrollregion()


