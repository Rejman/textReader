import tkinter as tk
from PIL import Image, ImageTk

class MainFrame(tk.Frame):
    WIDTH = 100
    HEIGHT = 100
    def __init__(self, master=None):
        super().__init__(master)
        self.config(width=MainFrame.WIDTH, height=MainFrame.HEIGHT)
        self.create_widgets()


    def create_widgets(self):
        self.create_buttons(pad_x=1, pad_y=5)
        self.create_textarea("Seqoe UI Light", 12)
        self.create_statusbar()

        self.set_layout()

    def create_textarea(self, font_name, font_size):

        # text area for input data
        self.text = tk.Text(self)
        self.text.configure(font=(font_name, font_size))

    def create_statusbar(self):
        # statusbar's frame
        self.statusbar_frame = tk.Frame(self)

        # labels
        self.info_label = tk.Label(self.statusbar_frame)
        self.info_label.config(text=" ")
        self.info_label.grid()

    def create_buttons(self, pad_x, pad_y):
        # images
        self.sound_png = tk.PhotoImage(file="png/sound.png")
        self.clear_png = tk.PhotoImage(file="png/clear.png")
        self.save_png = tk.PhotoImage(file="png/save.png")

        # button's frame
        self.buttons_frame = tk.Frame(self)

        # sound button
        self.sound_button = tk.Button(self.buttons_frame)
        self.sound_button.config(image=self.sound_png)
        self.sound_button.grid(row=0, column=1, padx=pad_x, pady=pad_y)
        # clear button
        self.clear_button = tk.Button(self.buttons_frame)
        self.clear_button.config(image=self.clear_png)
        self.clear_button.grid(row=0, column=2, padx=pad_x, pady=pad_y)
        # save button
        self.save_button = tk.Button(self.buttons_frame)
        self.save_button.config(image=self.save_png)
        self.save_button.grid(row=0, column=3, padx=pad_x, pady=pad_y)

    def set_layout(self):
        self.buttons_frame.grid(row=0, sticky=tk.E)
        self.text.grid(row=1, column=0, columnspan=1)
        self.statusbar_frame.grid(row=2, sticky=tk.E)

