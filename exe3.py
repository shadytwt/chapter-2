import tkinter as tk

root = tk.Tk()
root.title("Login Page")
root.geometry("350x180")
root.configure(bg="lightblue")

username_label = tk.Label(root, text="Username:", bg="lightblue", font=("Arial", 14))
username_label.grid(row=0, column=0, padx=(20,5), pady=15, sticky="e")  

username_entry = tk.Entry(root, font=("Arial", 14))
username_entry.grid(row=0, column=1, pady=15, sticky="w")  

password_label = tk.Label(root, text="Password:", bg="lightblue", font=("Arial", 14))
password_label.grid(row=1, column=0, padx=(20,5), pady=15, sticky="e")

password_entry = tk.Entry(root, show="*", font=("Arial", 14))
password_entry.grid(row=1, column=1, pady=15, sticky="w")

login_btn = tk.Button(root, text="Login", font=("Arial", 14), bg="skyblue")
login_btn.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()





