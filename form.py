import tkinter as tk
from tkinter import ttk
import os
import backend as source


root = tk.Tk()
root.geometry("560x450")

name_var = tk.StringVar()
name_lb = tk.Label(text="Name:", font=(29)).place(x=50,y=100)
name_entry = tk.Entry(width=40, textvariable=name_var)
name_entry.place(x=120, y=100)


class_var = tk.StringVar()
class_lb = tk.Label(text="Class:", font=(29)).place(x=50, y=200)

classes = [
    None,
    "J.s.s.1 (Grade7)",
    "J.s.s.2 (Grade8)",
    "J.s.s.3 (Grade9)",
    "S.S.S.1 (Grade10)",
    "S.S.S.2 (Grade11)",
    "S.S.S.3 (Grade12)"
]
classop2 = tk.StringVar()
class_options= ttk.OptionMenu(root,class_var,*classes)
class_options.place(x=120, y=200)
class_var.set("J.s.s.1 (Grade7)")

age_var = tk.StringVar()
age_ld = tk.Label(text="Age:", font=(29)).place(x=50, y=300)
age_entry = tk.Entry(width=40,textvariable=age_var)
age_entry.place(x=120, y=300)

def go(event):
    global name_res, class_res, age_res 
    name_res = name_var.get().strip()
    class_res = class_var.get().strip()
    age_res = age_var.get().strip()

    root.destroy()
    import main
    # print(name_res)
    # print(class_res)
    # print(age_res)

    

    # import main





# def go_2():
#     os.open("python3 /home/tom/Documents/My cbt system/form.py")

# go_2()

go_btn = tk.Button(text="Get started", command=lambda :go(go)).place(x=200,y=350)
all_entry = [name_entry, age_entry]

for entries in all_entry:
    entries.bind("<Return>",go)



root.mainloop()