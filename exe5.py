import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def perform_operation(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result = num1 / num2
        elif operation == "mod":
            if num2 == 0:
                messagebox.showerror("Error", "Modulo by zero is not allowed!")
                return
            result = num1 % num2
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def clear_fields():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="Result: ")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#e6ecf2")

title_label = tk.Label(root, text="Basic Calculator", font=("Arial", 18, "bold"), fg="#333366", bg="#e6ecf2")
title_label.pack(pady=20)

frame_inputs = ttk.Frame(root, padding="10")
frame_inputs.pack(pady=10)

ttk.Label(frame_inputs, text="Enter First Number:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_num1 = ttk.Entry(frame_inputs, width=25)
entry_num1.grid(row=0, column=1, pady=5)

ttk.Label(frame_inputs, text="Enter Second Number:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_num2 = ttk.Entry(frame_inputs, width=25)
entry_num2.grid(row=1, column=1, pady=5)

frame_buttons = ttk.Frame(root, padding="10")
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Add (+)", width=10, bg="#333366", fg="white",
                    command=lambda: perform_operation("add"))
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_sub = tk.Button(frame_buttons, text="Subtract (-)", width=10, bg="#333366", fg="white",
                    command=lambda: perform_operation("sub"))
btn_sub.grid(row=0, column=1, padx=5, pady=5)

btn_mul = tk.Button(frame_buttons, text="Multiply (×)", width=10, bg="#333366", fg="white",
                    command=lambda: perform_operation("mul"))
btn_mul.grid(row=1, column=0, padx=5, pady=5)

btn_div = tk.Button(frame_buttons, text="Divide (÷)", width=10, bg="#333366", fg="white",
                    command=lambda: perform_operation("div"))
btn_div.grid(row=1, column=1, padx=5, pady=5)

btn_mod = tk.Button(frame_buttons, text="Modulo (%)", width=10, bg="#333366", fg="white",
                    command=lambda: perform_operation("mod"))
btn_mod.grid(row=2, column=0, columnspan=2, pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 14), bg="#e6ecf2", fg="#222244")
result_label.pack(pady=20)

clear_button = tk.Button(root, text="Clear", width=12, bg="#555588", fg="white",
                         font=("Arial", 11, "bold"), command=clear_fields)
clear_button.pack(pady=10)

root.mainloop()
