#this GUIcode won"t Run it github I Guess because i don't lnow how to run this in Github


import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = 'users.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Interface")
        self.users = load_data()
        self.current_user = None

        self.login_screen()

    def login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="ATM Login", font=('Arial', 16)).pack(pady=10)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, "Username")

        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack(pady=5)
        self.pin_entry.insert(0, "1234")

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Create New User", command=self.create_user).pack()

    def login(self):
        username = self.username_entry.get()
        pin = self.pin_entry.get()

        if username in self.users and self.users[username]['pin'] == pin:
            self.current_user = username
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or PIN")

    def create_user(self):
        username = simpledialog.askstring("Username", "Enter new username:")
        pin = simpledialog.askstring("PIN", "Set 4-digit PIN:", show="*")
        if username in self.users:
            messagebox.showwarning("Warning", "User already exists!")
        else:
            self.users[username] = {'pin': pin, 'balance': 0.0, 'history': []}
            save_data(self.users)
            messagebox.showinfo("Success", "User created successfully!")

    def main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Welcome, {self.current_user}", font=('Arial', 16)).pack(pady=10)
        tk.Button(self.root, text="Check Balance", command=self.check_balance).pack(pady=5)
        tk.Button(self.root, text="Deposit Money", command=self.deposit).pack(pady=5)
        tk.Button(self.root, text="Withdraw Money", command=self.withdraw).pack(pady=5)
        tk.Button(self.root, text="Transaction History", command=self.show_history).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=5)

    def check_balance(self):
        balance = self.users[self.current_user]['balance']
        messagebox.showinfo("Balance", f"Your balance is ₹{balance:.2f}")

    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        if amount and amount > 0:
            self.users[self.current_user]['balance'] += amount
            self.users[self.current_user]['history'].append(f"Deposited ₹{amount:.2f}")
            save_data(self.users)
            messagebox.showinfo("Success", "Amount deposited successfully!")

    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        balance = self.users[self.current_user]['balance']
        if amount and amount > 0:
            if amount <= balance:
                self.users[self.current_user]['balance'] -= amount
                self.users[self.current_user]['history'].append(f"Withdrew ₹{amount:.2f}")
                save_data(self.users)
                messagebox.showinfo("Success", "Amount withdrawn successfully!")
            else:
                messagebox.showerror("Error", "Insufficient balance.")

    def show_history(self):
        history = self.users[self.current_user]['history']
        history_text = "\n".join(history) if history else "No transactions yet."
        messagebox.showinfo("Transaction History", history_text)

    def logout(self):
        self.current_user = None
        self.login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Start GUI App
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("300x400")
    app = ATMApp(root)
    root.mainloop()
