import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def c_to_f():
    try:
        c = float(temp_entry.get())
        f = (c * 9/5) + 32
        result_label.config(text=f"{c:.2f} °C = {f:.2f} °F")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid temperature in Celsius!")

def f_to_c():
    try:
        f = float(temp_entry.get())
        c = (f - 32) * 5/9
        result_label.config(text=f"{f:.2f} °F = {c:.2f} °C")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid temperature in Fahrenheit!")

def clear_fields():
    temp_entry.delete(0, tk.END)
    result_label.config(text="Result: ")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x350")
root.resizable(False, False)
root.config(bg="#e6ecf2")

title_label = tk.Label(
    root,
    text="Temperature Converter",
    font=("Arial", 18, "bold"),
    fg="#333366",
    bg="#e6ecf2"
)
title_label.pack(pady=20)

frame_input = ttk.Frame(root, padding="10")
frame_input.pack(pady=10)

ttk.Label(frame_input, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=5, sticky="w")

temp_entry = ttk.Entry(frame_input, width=25)
temp_entry.grid(row=0, column=1, pady=5)

frame_buttons = ttk.Frame(root, padding="10")
frame_buttons.pack(pady=15)

btn_c_to_f = tk.Button(
    frame_buttons,
    text="Celsius → Fahrenheit",
    width=18,
    bg="#333366",
    fg="white",
    command=c_to_f
)
btn_c_to_f.grid(row=0, column=0, padx=5, pady=5)

btn_f_to_c = tk.Button(
    frame_buttons,
    text="Fahrenheit → Celsius",
    width=18,
    bg="#333366",
    fg="white",
    command=f_to_c
)
btn_f_to_c.grid(row=0, column=1, padx=5, pady=5)

result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 14),
    bg="#e6ecf2",
    fg="#222244"
)
result_label.pack(pady=20)

clear_button = tk.Button(
    root,
    text="Clear",
    width=12,
    bg="#555588",
    fg="white",
    font=("Arial", 11, "bold"),
    command=clear_fields
)
clear_button.pack(pady=10)

root.mainloop()
