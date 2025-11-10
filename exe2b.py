import tkinter as tk

DARK_COLOR = "#22334f"
LIGHT_COLOR = "white"
FRAME_BORDER_WIDTH = 5

root = tk.Tk()
root.title("GUI Pack Example (Simplified)")
root.geometry("400x280")

frame_left = tk.Frame(
    root,
    bd=FRAME_BORDER_WIDTH,
    relief="raised"
)

frame_left.pack(side="left", fill="both", expand=True)

frame_right = tk.Frame(
    root,
    bd=FRAME_BORDER_WIDTH,
    relief="raised"
)

frame_right.pack(side="right", fill="both", expand=True)

label_a = tk.Label(
    frame_left, 
    text="A",
    bg=DARK_COLOR,
    fg=LIGHT_COLOR,
    font=("Inter", 15, "bold")
)

label_a.pack(side="top", fill="both", expand=True)

label_b = tk.Label(
    frame_left, 
    text="B",
    bg=LIGHT_COLOR,
    fg=DARK_COLOR,
    font=("Inter", 15, "bold")
)

label_b.pack(side="bottom", fill="both", expand=True)

label_c = tk.Label(
    frame_right, 
    text="C",
    bg=LIGHT_COLOR,
    fg=DARK_COLOR,
    font=("Inter", 15, "bold")
)

label_c.pack(side="top", fill="both", expand=True)

label_d = tk.Label(
    frame_right, 
    text="D",
    bg=DARK_COLOR,
    fg=LIGHT_COLOR,
    font=("Inter", 15, "bold")
)

label_d.pack(side="bottom", fill="both", expand=True)

root.mainloop()