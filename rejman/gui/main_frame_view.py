import tkinter as tk

class MainFrame(tk.Frame):
    WIDTH = 100
    HEIGHT = 100
    def __init__(self, master=None):
        super().__init__(master)
        self.config(width=MainFrame.WIDTH, height=MainFrame.HEIGHT)
        self.create_widgets()



    def create_widgets(self):
        self.create_menu(pad_x=5, pad_y=5, space=0)
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

    def create_menu(self, pad_x, pad_y, space):
        # images
        self.sound_png = tk.PhotoImage(file="png/sound.png")
        self.clear_png = tk.PhotoImage(file="png/clear.png")
        self.save_png = tk.PhotoImage(file="png/save.png")

        # button's frame
        self.menu_frame = tk.Frame(self)

        # volume scale
        self.volume_scale = tk.Scale(self.menu_frame, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=0, label="Volume:")
        self.volume_scale.config(length=200, sliderlength=20, width=10)
        self.volume_scale.set(50)
        self.volume_scale.grid(row=0, column=0)
        # sound button
        self.sound_button = tk.Button(self.menu_frame)
        self.sound_button.config(image=self.sound_png)
        self.sound_button.grid(row=0, column=1, padx=(pad_x,0), pady=pad_y)
        # clear button
        self.clear_button = tk.Button(self.menu_frame)
        self.clear_button.config(image=self.clear_png)
        self.clear_button.grid(row=0, column=2, padx=space, pady=pad_y)
        # save button
        self.save_button = tk.Button(self.menu_frame)
        self.save_button.config(image=self.save_png)
        self.save_button.grid(row=0, column=3, padx=(0,pad_x), pady=pad_y)

    def set_layout(self):

        self.menu_frame.grid(row=0, column=1, sticky=tk.E)
        self.text.grid(row=1, column=0, columnspan=2, padx=5)
        self.statusbar_frame.grid(row=2, sticky=tk.E)




