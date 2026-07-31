#Practical no 6
#Ekta S078
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class PriorityQueue:
    def __init__(self, max_capacity):
        self.queue = []
        self.max_capacity = max_capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.max_capacity

    def enqueue(self, item, priority):
        if self.is_full():
            print(Fore.RED + "Priority Queue is full. Cannot enqueue.")
            return

        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])  # Sort by priority

        print(Fore.GREEN + f"Enqueued: {item} with priority {priority}")

    def dequeue(self):
        if self.is_empty():
            print(Fore.RED + "Priority Queue is empty. Cannot dequeue.")
            return

        item, priority = self.queue.pop(0)
        print(Fore.GREEN + f"Dequeued: {item}")

    def traverse(self):
        if self.is_empty():
            print(Fore.YELLOW + "Priority Queue is empty.")
        else:
            print(Fore.CYAN + "Priority Queue contains:")
            for item, priority in self.queue:
                print(Fore.CYAN + f"Item: {item}, Priority: {priority}")

    def show_ascending(self):
        if self.is_empty():
            print(Fore.YELLOW + "Priority Queue is empty.")
        else:
            print(Fore.CYAN + "Priority Queue in Ascending Order:")
            for item, priority in sorted(self.queue, key=lambda x: x[1]):
                print(Fore.CYAN + f"Item: {item}, Priority: {priority}")

    def show_descending(self):
        if self.is_empty():
            print(Fore.YELLOW + "Priority Queue is empty.")
        else:
            print(Fore.CYAN + "Priority Queue in Descending Order:")
            for item, priority in sorted(self.queue, key=lambda x: x[1], reverse=True):
                print(Fore.CYAN + f"Item: {item}, Priority: {priority}")


def main():

    while True:
        try:
            max_capacity = int(input("Enter the maximum capacity of the Priority Queue: "))
            break
        except ValueError:
            print(Fore.RED + "Please enter a valid integer.")

    pq = PriorityQueue(max_capacity)

    while True:

        print(Fore.YELLOW + "\nPriority Queue Menu:")
        print(Fore.YELLOW + "1. Enqueue")
        print(Fore.YELLOW + "2. Dequeue")
        print(Fore.YELLOW + "3. Traverse")
        print(Fore.YELLOW + "4. Check if Empty")
        print(Fore.YELLOW + "5. Check if Full")
        print(Fore.YELLOW + "6. Show Ascending Order")
        print(Fore.YELLOW + "7. Show Descending Order")
        print(Fore.YELLOW + "8. Exit")

        try:
            choice = int(input(Fore.BLUE + "Enter your choice: "))
        except ValueError:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 8.")
            continue

        if choice == 1:
            item = input(Fore.BLUE + "Enter item to enqueue: ")
            try:
                priority = int(input(Fore.BLUE + "Enter priority: "))
                pq.enqueue(item, priority)
            except ValueError:
                print(Fore.RED + "Priority must be an integer.")

        elif choice == 2:
            pq.dequeue()

        elif choice == 3:
            pq.traverse()

        elif choice == 4:
            if pq.is_empty():
                print(Fore.CYAN + "Priority Queue is empty.")
            else:
                print(Fore.CYAN + "Priority Queue is not empty.")

        elif choice == 5:
            if pq.is_full():
                print(Fore.CYAN + "Priority Queue is full.")
            else:
                print(Fore.CYAN + "Priority Queue is not full.")

        elif choice == 6:
            pq.show_ascending()

        elif choice == 7:
            pq.show_descending()

        elif choice == 8:
            print(Fore.RED + "Exiting...")
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
