import tkinter as tk

root = tk.Tk()
root.title("GUI Pack Example")
root.geometry("215x77")
root.config(bg="#e0e0e0")

label_a = tk.Label(root, text="A", bg="red", bd=6, relief="ridge")

label_b = tk.Label(root, text="B", bg="yellow", bd=5, relief="raised", width=15)
label_b.pack(side="bottom")

label_c = tk.Label(root, text="C", bg="blue", width=15)
label_d = tk.Label(root, text="D", bg="white", width=15)

def reposition(event=None):
    w = root.winfo_width()
    h = root.winfo_height()

    if w <= 215 and h <= 77:
        label_a.place(x=0, y=0, width=w)  
    else:
        label_a.place(x=0, y=h//2 - 15, width=w)  

    if w <= 215:
        label_c.place(x=0, y=h - 48)
    else:
        label_c.place(x=w - 880, y=h - 48)

    label_d.place(x=w - 110, y=h - 48)

root.bind("<Configure>", reposition)

reposition()

root.mainloop()





