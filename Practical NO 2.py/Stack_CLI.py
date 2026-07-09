class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into stack.")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped element:", self.stack.pop())

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Top Element:", self.stack[-1])

    def traverse(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack Elements (Top to Bottom):")
            for item in reversed(self.stack):
                print(item)


stack = Stack()

while True:
    print("\n===== STACK MENU =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Traverse")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter element: ")
        stack.push(item)

    elif choice == "2":
        stack.pop()

    elif choice == "3":
        stack.peek()

    elif choice == "4":
        stack.traverse()

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")
