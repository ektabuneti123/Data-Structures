#Name - ekta buneti
#roll no  - S078
import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item):
        if len(self.queue) >= self.size:
            return False
        self.queue.append(item)
        return True

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def traverse(self):
        return self.queue


queue = Queue(5)

def insert():
    item = entry.get()
    if item == "":
        return

    if queue.enqueue(item):
        update_display()
    else:
        messagebox.showerror("Error", "Queue Full")

    entry.delete(0, tk.END)

def delete():
    item = queue.dequeue()

    if item is None:
        messagebox.showerror("Error", "Queue Empty")
    else:
        messagebox.showinfo("Deleted", f"{item} removed")

    update_display()

def peek():
    item = queue.peek()

    if item is None:
        messagebox.showerror("Error", "Queue Empty")
    else:
        messagebox.showinfo("Front", item)

def update_display():
    display.config(text=str(queue.traverse()))

root = tk.Tk()
root.title("Queue Implementation")

tk.Label(root, text="Enter Item").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Enqueue", command=insert).pack(pady=5)

tk.Button(root, text="Dequeue", command=delete).pack(pady=5)

tk.Button(root, text="Peek", command=peek).pack(pady=5)

display = tk.Label(root, text="[]", font=("Arial", 14))
display.pack(pady=10)

update_display()

root.mainloop()
