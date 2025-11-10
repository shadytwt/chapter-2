import tkinter as tk
from tkinter import ttk

def submit_form():
    print("Form Submitted!")

def clear_form():
    print("Form Cleared!")
    student_name_entry.delete(0, tk.END)
    mobile_number_entry.delete(0, tk.END)
    email_id_entry.delete(0, tk.END)
    home_address_entry.delete(0, tk.END)
    gender_combobox.set("Select Gender")
    selected_course.set("")
    english_checkbox.deselect()
    tagalog_checkbox.deselect()
    hindi_urdu_checkbox.deselect()
    communication_scale.set(0)

root = tk.Tk()
root.title("Student Management System")
root.geometry("500x750")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

banner_frame = tk.Frame(main_frame, bg="#333366", height=100)
banner_frame.pack(fill=tk.X, pady=(0, 20))

inner_border = tk.Frame(banner_frame, bg="white", height=90)
inner_border.pack(padx=8, pady=8, fill=tk.BOTH, expand=True)

inner_content = tk.Frame(inner_border, bg="#333366")
inner_content.pack(padx=4, pady=4, fill=tk.BOTH, expand=True)

banner_label = tk.Label(
    inner_content,
    text="Bath Spa University",
    bg="#333366",
    fg="white",
    font=("Arial", 22, "bold")
)
banner_label.pack(expand=True, fill=tk.BOTH)

subtitle_banner = tk.Label(
    inner_content,
    text="RAK Campus",
    bg="#444488",
    fg="white",
    font=("Arial", 12)
)
subtitle_banner.pack(fill=tk.X)

title_label = tk.Label(
    main_frame,
    text="Student Management System",
    font=("Arial", 16, "bold"),
    fg="#333366"
)
title_label.pack(pady=(0, 0))

subtitle_label = ttk.Label(
    main_frame,
    text="New Student Registration",
    font=("Arial", 14)
)
subtitle_label.pack(pady=(0, 20))

form_frame = ttk.Frame(main_frame)
form_frame.pack(fill=tk.X, pady=10)

def create_entry_row(parent, label_text):
    row_frame = ttk.Frame(parent)
    row_frame.pack(fill=tk.X, pady=5)
    label = ttk.Label(row_frame, text=label_text, width=15, anchor="w", font=("Arial", 10))
    label.pack(side=tk.LEFT, padx=(0, 10))
    entry = ttk.Entry(row_frame, width=40)
    entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
    return entry

student_name_entry = create_entry_row(form_frame, "Student Name:")
mobile_number_entry = create_entry_row(form_frame, "Mobile Number:")
email_id_entry = create_entry_row(form_frame, "Email Id:")
home_address_entry = create_entry_row(form_frame, "Home Address:")

gender_frame = ttk.Frame(form_frame)
gender_frame.pack(fill=tk.X, pady=5)
gender_label = ttk.Label(gender_frame, text="Gender:", width=15, anchor="w", font=("Arial", 10))
gender_label.pack(side=tk.LEFT, padx=(0, 10))
gender_options = ["Male", "Female", "Other"]
gender_combobox = ttk.Combobox(gender_frame, values=gender_options, state="readonly", width=37)
gender_combobox.set("Select Gender")
gender_combobox.pack(side=tk.RIGHT, expand=True, fill=tk.X)

course_frame = ttk.Frame(form_frame)
course_frame.pack(fill=tk.X, pady=10)
course_label = ttk.Label(course_frame, text="Course Enrolled:", width=15, anchor="w", font=("Arial", 10))
course_label.pack(side=tk.LEFT, padx=(0, 10), anchor="n")

course_radio_frame = ttk.Frame(course_frame)
course_radio_frame.pack(side=tk.LEFT, anchor="n", pady=2)

selected_course = tk.StringVar(value="")
courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]
for course in courses:
    rb = ttk.Radiobutton(course_radio_frame, text=course, variable=selected_course, value=course)
    rb.pack(anchor="w", pady=2)

languages_frame = ttk.Frame(form_frame)
languages_frame.pack(fill=tk.X, pady=10)
languages_label = ttk.Label(languages_frame, text="Languages known:", width=15, anchor="w", font=("Arial", 10))
languages_label.pack(side=tk.LEFT, padx=(0, 10), anchor="n")

checkbox_frame = ttk.Frame(languages_frame)
checkbox_frame.pack(side=tk.LEFT, anchor="n", pady=2)

english_var = tk.BooleanVar()
tagalog_var = tk.BooleanVar()
hindi_urdu_var = tk.BooleanVar()

english_checkbox = ttk.Checkbutton(checkbox_frame, text="English", variable=english_var)
english_checkbox.grid(row=0, column=0, sticky="w", padx=5)
tagalog_checkbox = ttk.Checkbutton(checkbox_frame, text="Tagalog", variable=tagalog_var)
tagalog_checkbox.grid(row=0, column=1, sticky="w", padx=5)
hindi_urdu_checkbox = ttk.Checkbutton(checkbox_frame, text="Hindi/Urdu", variable=hindi_urdu_var)
hindi_urdu_checkbox.grid(row=1, column=0, sticky="w", padx=5, columnspan=2)

communication_frame = ttk.Frame(form_frame)
communication_frame.pack(fill=tk.X, pady=10)
communication_label = ttk.Label(
    communication_frame,
    text="Rate your English communication skills",
    font=("Arial", 10)
)
communication_label.pack(anchor="w", pady=(0, 5))
communication_scale = ttk.Scale(communication_frame, from_=0, to=10, orient="horizontal", length=400)
communication_scale.set(5)
communication_scale.pack(fill=tk.X, expand=True)

button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

button_width = 12

submit_button = tk.Button(
    button_frame, text="Submit", command=submit_form,
    bg="#333366", fg="white", font=("Arial", 12, "bold"),
    activebackground="#555588", activeforeground="white",
    width=button_width
)
submit_button.pack(side=tk.LEFT, padx=10, ipadx=20, ipady=10)

clear_button = tk.Button(
    button_frame, text="Clear", command=clear_form,
    bg="#333366", fg="white", font=("Arial", 12, "bold"),
    activebackground="#555588", activeforeground="white",
    width=button_width
)
clear_button.pack(side=tk.RIGHT, padx=10, ipadx=20, ipady=10)

root.mainloop()







