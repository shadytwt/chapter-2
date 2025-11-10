import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime

def calculate_age():
    dob_str = dob_entry.get()
    try:
        dob = datetime.strptime(dob_str, "%d/%m/%Y").date()
        today = date.today()

        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        if age < 0:
            messagebox.showerror("Error", "Date of birth cannot be in the future!")
            return
        
        result_label.config(text=f"Your age is {age} years")
    except ValueError:
        messagebox.showerror("Error", "Please enter date in DD/MM/YYYY format!")

def clear_fields():
    dob_entry.delete(0, tk.END)
    result_label.config(text="Result: ")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="#e6ecf2")

title_label = tk.Label(
    root,
    text="Age Calculator",
    font=("Arial", 18, "bold"),
    fg="#333366",
    bg="#e6ecf2"
)
title_label.pack(pady=20)

frame_input = ttk.Frame(root, padding="10")
frame_input.pack(pady=10)

ttk.Label(frame_input, text="Enter Date of Birth (DD/MM/YYYY):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
dob_entry = ttk.Entry(frame_input, width=25)
dob_entry.grid(row=0, column=1, pady=5)

frame_buttons = ttk.Frame(root, padding="10")
frame_buttons.pack(pady=15)

calc_button = tk.Button(
    frame_buttons,
    text="Calculate Age",
    width=15,
    bg="#333366",
    fg="white",
    command=calculate_age
)
calc_button.grid(row=0, column=0, padx=10, pady=5)

clear_button = tk.Button(
    frame_buttons,
    text="Clear",
    width=10,
    bg="#555588",
    fg="white",
    command=clear_fields
)
clear_button.grid(row=0, column=1, padx=10, pady=5)

result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 14),
    bg="#e6ecf2",
    fg="#222244"
)
result_label.pack(pady=20)

root.mainloop()

