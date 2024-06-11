from tkinter import *
from tkinter import filedialog
import im


class MyWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title("Edit Image")
        self.win.configure(bg='#FFA0CB')
        self.img = None

        self.btn1 = Button(self.win, text="Upload Image", width=15, height=3, background="pink", command=self.upload_image)
        self.btn2 = Button(self.win, text="Filters", width=15, height=3, background="pink" , command=self.filter)
        self.btn3 = Button(self.win, text="Cut", width=15, height=3, background="pink", command=self.cut)
        self.btn4 = Button(self.win, text="Add Text", width=15, height=3, background="pink", command=self.text)
        self.btn5 = Button(self.win, text="Add Shape", width=15, height=3, background="pink", command=self.draw)
        self.btn6 = Button(self.win, text="Rotate", width=15, height=3, background="pink", command= self.rotate)
        self.btn7 = Button(self.win, text="Save as", width=15, height=3, background="pink", command=self.save_image)
        self.btn8 = Button(self.win, text="Exit", width=15, height=3, background="pink", command=self.exit_application)

        self.positions()
        self.win.mainloop()

    def positions(self):
        self.btn1.grid(row=0, column=0, padx=20, pady=10)
        self.btn2.grid(row=0, column=1, padx=20, pady=10)
        self.btn3.grid(row=1, column=0, padx=20, pady=10)
        self.btn4.grid(row=1, column=1, padx=20, pady=10)
        self.btn5.grid(row=2, column=0, padx=20, pady=10)
        self.btn6.grid(row=2, column=1, padx=20, pady=10)
        self.btn7.grid(row=3, column=0, padx=20, pady=10)
        self.btn8.grid(row=3, column=1, padx=20, pady=10)

    def exit_application(self):
        self.win.destroy()  # close window

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("נבחרה תמונה:", file_path)
            self.img = im.MyImage(file_path, "window1")

    def text(self):
        self.img.add_text()

    def rotate(self):
        self.img.rotate()

    def filter(self):
        self.img.filter()

    def draw(self):
        self.img.draw_rec()

    def cut(self):
        self.img.cut()

    def save_image(self):
        if self.img is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.img.save_image(file_path)
                print("Image saved successfully.")
            else:
                print("Save operation canceled.")
        else:
            print("No image loaded.")

    def close_window(self):
        self.win.destroy()


w = MyWindow()
