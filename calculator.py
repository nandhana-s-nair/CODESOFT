import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.resizable(False, False)
tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Enter First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack(pady=5)
tk.Label(root, text="Enter Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="+", width=5, command=lambda: calculate("+")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="-", width=5, command=lambda: calculate("-")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="*", width=5, command=lambda: calculate("*")).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="/", width=5, command=lambda: calculate("/")).grid(row=0, column=3, padx=5)
result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack(pady=10)
root.mainloop()