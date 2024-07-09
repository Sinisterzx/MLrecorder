import tkinter as tk
from fileinput import filename
from tkinter import filedialog
from Analysis import Analysis


class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title("MLRecorder")
        self.root.configure(bg='black')

    def button_0(self):
        filename = filedialog.askopenfilename(initialdir = '/',
                                              title = "Select a File",
                                              filetypes = [("JPEG",
                                                            "*.jpg")])

        analysis = Analysis(filename)
        analysis.recognition()


    def launch(self):
        button = tk.Button(self.root, text="Click Me", command=self.button_0)
        button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.root.mainloop()




