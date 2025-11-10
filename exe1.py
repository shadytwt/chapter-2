import tkinter as tk

root = tk.Tk()
root.title("Welcome App")

root.geometry("400x200")

root.resizable(False, False)

root.configure(bg="#87CEEB")  

welcome_label = tk.Label(root, text="Welcome to Python GUI!", 
                         font=("Arial", 20, "bold"), 
                         bg="#87CEEB")
welcome_label.pack(pady=50)

root.mainloop()
