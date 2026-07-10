# S078 Ekta Buneti
# Aim: Write a Python program to implement Doubly Linked List
# with insertion, deletion, traversal, searching and length operations.

import time
from colorama import init, Fore, Style

init(autoreset=True, convert=True)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        


class DoublyList:
    def __init__(self):
        self.head = None

    def insert_begin(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.previous = current

    def insert_position(self, value, position):

        if position == 0:
            self.insert_begin(value)
            return

        new_node = Node(value)
        current = self.head

        for _ in range(position):
            if current is None:
                raise IndexError("Invalid position.")
            current = current.next

        if current is None:
            raise IndexError("Invalid position.")

        new_node.next = current
        new_node.previous = current.previous

        if current.previous:
            current.previous.next = new_node

        current.previous = new_node

    def delete_begin(self):

        if self.head is None:
            print(Fore.YELLOW + "List is empty.")
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.previous = None

    def delete_end(self):

        if self.head is None:
            print(Fore.YELLOW + "List is empty.")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next:
            current = current.next

        current.previous.next = None

    def delete_position(self, position):

        if self.head is None:
            print(Fore.YELLOW + "List is empty.")
            return

        current = self.head

        for _ in range(position):
            if current is None:
                raise IndexError("Invalid position.")
            current = current.next

        if current is None:
            raise IndexError("Invalid position.")

        if current.previous:
            current.previous.next = current.next

        if current.next:
            current.next.previous = current.previous

    def traverse(self):

        if self.head is None:
            print(Fore.RED + "Doubly Linked List is empty.")
            return

        print(Fore.GREEN + "Doubly Linked List:")

        current = self.head

        while current:
            print(current.value, end=" <-> ")
            current = current.next

        print("None")

    def search(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def length(self):

        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

def display_menu():
    print("\n" + Style.BRIGHT + "===== Doubly Linked List Menu =====")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Traverse List")
    print("8. Search Element")
    print("9. Display Length")
    print("10. Exit")


def main():
    linked_list = DoublyList()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                value = int(input("Enter value: "))
                linked_list.insert_begin(value)
                print(Fore.GREEN + "Node inserted at beginning.")

            elif choice == 2:
                value = int(input("Enter value: "))
                linked_list.insert_end(value)
                print(Fore.GREEN + "Node inserted at end.")

            elif choice == 3:
                value = int(input("Enter value: "))
                position = int(input("Enter position: "))
                linked_list.insert_position(value, position)
                print(Fore.GREEN + "Node inserted successfully.")

            elif choice == 4:
                linked_list.delete_begin()
                print(Fore.RED + "First node deleted.")

            elif choice == 5:
                linked_list.delete_end()
                print(Fore.RED + "Last node deleted.")

            elif choice == 6:
                position = int(input("Enter position to delete: "))
                linked_list.delete_position(position)
                print(Fore.RED + "Node deleted successfully.")

            elif choice == 7:
                linked_list.traverse()

            elif choice == 8:
                value = int(input("Enter value to search: "))

                if linked_list.search(value):
                    print(Fore.GREEN + "Value found in the list.")
                else:
                    print(Fore.RED + "Value not found.")

            elif choice == 9:
                print(Fore.CYAN + f"Total Nodes: {linked_list.length()}")

            elif choice == 10:
                print("Program Closed.")
                break

            else:
                print(Fore.YELLOW + "Invalid choice.")

        except ValueError:
            print(Fore.RED + "Please enter valid integers.")

        except IndexError as error:
            print(Fore.RED + str(error))

        except Exception as error:
            print(Fore.RED + str(error))

        time.sleep(1)


if __name__ == "__main__":
    main()
