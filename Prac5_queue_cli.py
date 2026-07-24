#Name - ekta buneti
#roll no  - S078
#CLI Version
import os
from colorama import Fore, init

init(autoreset=True)

class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            print(Fore.RED + "Queue is Full!")
        else:
            self.queue.append(item)
            print(Fore.GREEN + f"{item} inserted.")

    def dequeue(self):
        if self.is_empty():
            print(Fore.RED + "Queue is Empty!")
        else:
            item = self.queue.pop(0)
            print(Fore.YELLOW + f"{item} deleted.")

    def peek(self):
        if self.is_empty():
            print(Fore.RED + "Queue is Empty!")
        else:
            print(Fore.CYAN + f"Front Item: {self.queue[0]}")

    def traverse(self):
        if self.is_empty():
            print(Fore.RED + "Queue is Empty!")
        else:
            print(Fore.BLUE + "Queue:", " -> ".join(map(str, self.queue)))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    size = int(input("Enter Queue Size: "))
    q = Queue(size)

    while True:
        clear()
        print("\nQUEUE MENU")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Traverse")
        print("5. Is Empty")
        print("6. Is Full")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            item = input("Enter Item: ")
            q.enqueue(item)

        elif choice == "2":
            q.dequeue()

        elif choice == "3":
            q.peek()

        elif choice == "4":
            q.traverse()

        elif choice == "5":
            print("Queue Empty" if q.is_empty() else "Queue Not Empty")

        elif choice == "6":
            print("Queue Full" if q.is_full() else "Queue Not Full")

        elif choice == "7":
            break

        else:
            print("Invalid Choice")

        input("\nPress Enter...")
