from tkinter import *
from tkinter import messagebox
import math

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
        self.history_list = []  # History storage

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if '.' in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            expression = f"{self.total} {self.op_symbol()} {self.current}"
            self.valid_function()
            self.history_list.append(f"{expression} = {self.total}")
        else:
            self.total = float(txtDisplay.get())

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "mul":
            self.total *= self.current
        if self.op == "divide":
            if self.current != 0:
                self.total /= self.current
            else:
                self.display("Error")
                return
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        if self.current != "":
            self.current = float(self.current)
            if self.check_sum:
                self.valid_function()
            elif not self.result:
                self.total = self.current
        self.op = op
        self.input_value = True
        self.check_sum = True
        self.result = False
        self.display(0)

    def op_symbol(self):
        symbols = {"add": "+", "sub": "-", "mul": "*", "divide": "/"}
        return symbols.get(self.op, self.op)

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def sign(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def square(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def show_history(self):
        if not self.history_list:
            messagebox.showinfo("History", "No calculations yet.")
        else:
            messagebox.showinfo("History", "\n".join(self.history_list))


added_value = Calc()

root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)
calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

def btnClick(numbers):
    added_value.numberEnter(numbers)

def btnCommand(op):
    added_value.operation(op)

def btnEquals():
    added_value.sum_of_total()

# Row 1
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="CE", bg="red", command=added_value.all_Clear_Entry).grid(row=1, column=0)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="C", bg="white", command=added_value.Clear_Entry).grid(row=1, column=1)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="√", bg="white", command=added_value.square).grid(row=1, column=2)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="+", bg="white", command=lambda: btnCommand("add")).grid(row=1, column=3)

# Row 2
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2, column=0)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2, column=1)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2, column=2)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="-", bg="white", command=lambda: btnCommand("sub")).grid(row=2, column=3)

# Row 3
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3, column=0)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3, column=1)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=3, column=2)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="*", bg="white", command=lambda: btnCommand("mul")).grid(row=3, column=3)

# Row 4
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=4, column=0)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4, column=1)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4, column=2)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="/", bg="white", command=lambda: btnCommand("divide")).grid(row=4, column=3)

# Row 5
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="0", bg="white", command=lambda: btnClick(0)).grid(row=5, column=0)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text=".", bg="white", command=lambda: btnClick('.')).grid(row=5, column=1)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text=chr(177), bg="white", command=added_value.sign).grid(row=5, column=2)
Button(calc, pady=1, bd=4, fg="black", font=("arial", 20, "bold"), width=6, height=2, text="=", bg="blue", command=btnEquals).grid(row=5, column=3)

# Row 6 - History Button
Button(calc, pady=1, bd=4, fg="black", font=("arial", 16, "bold"), width=36, height=1, text="History", bg="light yellow", command=added_value.show_history).grid(row=6, column=0, columnspan=4)

root.mainloop()
