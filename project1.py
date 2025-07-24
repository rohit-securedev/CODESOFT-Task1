import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4.")
        return

    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        messagebox.showerror("Error", "Select at least one character type.")
        return

    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    password += random.choices(character_pool, k=length - len(password))
    random.shuffle(password)

    final_password = ''.join(password)
    result_var.set(final_password)

def copy_to_clipboard():
    password = result_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

app = tk.Tk()
app.title("🔐 Password Generator")
app.geometry("400x380")
app.config(padx=20, pady=20, bg="#f7f7f7")

tk.Label(app, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#f7f7f7").pack(pady=10)

length_var = tk.IntVar(value=12)
tk.Label(app, text="Password Length:", bg="#f7f7f7").pack()
tk.Entry(app, textvariable=length_var, width=5, font=("Helvetica", 12)).pack(pady=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(app, text="Include Uppercase Letters", variable=upper_var, bg="#f7f7f7").pack(anchor='w')
tk.Checkbutton(app, text="Include Lowercase Letters", variable=lower_var, bg="#f7f7f7").pack(anchor='w')
tk.Checkbutton(app, text="Include Digits", variable=digits_var, bg="#f7f7f7").pack(anchor='w')
tk.Checkbutton(app, text="Include Symbols", variable=symbols_var, bg="#f7f7f7").pack(anchor='w')

tk.Button(app, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold")).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(app, textvariable=result_var, width=30, font=("Helvetica", 12), justify='center').pack(pady=10)

tk.Button(app, text="Copy Password", command=copy_to_clipboard, bg="#2196F3", fg="white", font=("Helvetica", 11)).pack(pady=5)

app.mainloop()
