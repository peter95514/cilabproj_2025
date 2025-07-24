import tkinter as tk 
from tkinter import filedialog

def Button_file():
    file_path = filedialog.askopenfilename(
        title="chose file",
    ) 
    return file_path 

def Button_dir():
    file_path = filedialog.askdirectory(
        title="chose dir",
    ) 
    return file_path 


def create_tk():

    window = tk.Tk()
    window.title("temp")
    window.geometry("800x600")

    menu = tk.Menu(window)
    window.config(menu=menu)
    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="file", menu=file_menu)
    file_menu.add_command(label="new file", command=Button_file)
    file_menu.add_command(label="new dir", command=Button_dir)
    file_menu.add_separator()
    file_menu.add_command(label="exit", command=window.quit)

    window.mainloop()

    return

create_tk()
