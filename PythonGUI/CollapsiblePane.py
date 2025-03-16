import tkinter as tk
from tkinter import ttk
 
class CollapsiblePane(ttk.Frame):

    def __init__(self, parent, expanded_text ="Collapse <<", collapsed_text ="Expand >>", bg="black", fg="white", State="NORMAL"):
 
        ttk.Frame.__init__(self, parent)

        self.parent = parent
        self._expanded_text = expanded_text
        self._collapsed_text = collapsed_text
        self._fg= fg
        self._bg= bg
        self.State= State

        self.columnconfigure(1, weight = 1)

        self.CFrame_style= ttk.Style()
        self.CFrame_style.configure("CFrStyle.TFrame", background="#1f1f1f")
        self.C_frame=ttk.Frame(self, relief="flat", style="CFrStyle.TFrame")
        self.C_frame.grid(row = 0, column = 1, sticky='nsew')
        #--------------------------------------------------------------------
        #self.LFrame_style= ttk.Style()                                        
        #self.LFrame_style.configure("LFrStyle.TFrame", borderwidth=2)
        self.Frame_Frame=tk.Frame(self, background=self._bg, borderwidth=2)
        self.Frame_Frame.grid(row = 0, column = 0, sticky="w")
        self.Label_Frame=tk.Frame(self.Frame_Frame, background=self._fg, borderwidth=1)
        self.Label_Frame.pack()
        #--------------------------------------------------------------------
        self._styleClose=ttk.Style()
        self._styleClose.configure("_styleClose.TLabel", foreground=self._fg, background=self._bg)
        self._styleOpen=ttk.Style()
        self._styleOpen.configure("_styleOpen.TLabel", foreground=self._bg, background=self._fg)
        self._variable = tk.IntVar()
        self._button = ttk.Checkbutton(self.Label_Frame, variable = self._variable, command = self._activate, takefocus=False)
        self._button.pack()
        if(self.State=="NORMAL"):
            self._button.state(['!disabled'])
        elif(self.State=="DISABLED"):
            self._button.state(['disabled'])
        #self._separator = ttk.Separator(self, orient ="horizontal")
        #self._separator.grid(row = 0, column = 1, sticky ="we")
              
        self.frame = tk.Frame(self, bg="#1f1f1f", highlightbackground="#555555", highlightthickness=1)
        #self.Empty_Frame=tk.Label(self.frame, text="Empty", bg="#1f1f1f", fg="black")

        self._activate()
 
    def _activate(self):
        if not self._variable.get():
            #default value of Checkbutton is 0
            self.frame.grid_forget()
            self._button.configure(text = self._collapsed_text, style='_styleClose.TLabel')
            self.Frame_Frame.configure(background=self._bg, borderwidth=1)
            self.Label_Frame.configure(background=self._fg, borderwidth=0.5)
        elif self._variable.get():
            self.frame.grid(row = 1, column = 0, columnspan=2, pady=0.5)
            self._button.configure(text = self._expanded_text, style='_styleOpen.TLabel')
            self.Frame_Frame.configure(background=self._fg, borderwidth=1)
            self.Label_Frame.configure(background=self._bg, borderwidth=0.5)

    def toggle(self):
        self._variable.set(not self._variable.get())
        self._activate()
    
    def _isactive(self):
        if(self._variable.get()):
            return True
        else:
            return False

    def no_kin(self):
        if(len(self.frame.winfo_children())==0):
            self._variable.set(0)
            self._activate()
            self.frame.grid_remove()
            
    def _change(self, NewState="NORMAL"):
            self.State= NewState
            if(self.State=="NORMAL"):
                self._button.state(['!disabled'])
            elif(self.State=="DISABLED"):
             self._button.state(['disabled'])
    