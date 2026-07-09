import tkinter as tk
from tkinter import messagebox

stack = []


def push():
    item = entry.get()
    if item == "":
        messagebox.showwarning("Warning", "Enter a value")
        return
    stack.append(item)
    entry.delete(0, tk.END)
    display()


def pop():
    if not stack:
        messagebox.showerror("Error", "Stack Underflow")
    else:
        messagebox.showinfo("Popped", f"Popped Item: {stack.pop()}")
        display()


def traverse():
    if not stack:
        messagebox.showinfo("Stack", "Stack is Empty")
    else:
        messagebox.showinfo(
            "Stack Elements",
            "\n".join(reversed(stack))
        )


def clear_stack():
    stack.clear()
    display()


def display():
    if stack:
        label.config(text="Top -> " + " | ".join(reversed(stack)))
    else:
        label.config(text="Stack is Empty")


root = tk.Tk()
root.title("Stack Operations Using GUI")
root.geometry("400x350")

tk.Label(root, text="Enter Element", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=25)
entry.pack()

tk.Button(root, text="Push", width=15, command=push).pack(pady=5)
tk.Button(root, text="Pop", width=15, command=pop).pack(pady=5)
tk.Button(root, text="Traverse", width=15, command=traverse).pack(pady=5)
tk.Button(root, text="Clear Stack", width=15, command=clear_stack).pack(pady=5)

label = tk.Label(root, text="Stack is Empty", fg="blue", font=("Arial", 11))
label.pack(pady=20)

root.mainloop()
