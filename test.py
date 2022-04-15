import tkinter as tk

i = 0

def init_value(evt):
    global i
    i = 0
    
def increase_value():
    global i
    print(i)
    i += 1
    

bt = tk.Button(text="press", command=increase_value, repeatdelay=20, repeatinterval=50)
bt.pack()

bt.bind('<ButtonRelease-1>', init_value)

tk.mainloop()