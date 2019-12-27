# -*- coding: utf-8 -*-
import tkinter as tk

from rejman.gui.main_frame_view import MainFrame


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.grid()
        self.main_frame = MainFrame(self.master).grid()

root = tk.Tk()
# sys.setdefaultencoding("windows-1250")
root.tk.call('encoding', 'system', 'utf-8')
root.title("KonradReader (Alfa)")
app = Application(master=root)
app.mainloop()