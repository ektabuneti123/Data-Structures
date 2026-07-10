#S078EKtaBuneti
#Aim: write a program to implement singly link list with insertion,
#deletion, traversal operations

import time
from colorama import init, Fore, Style

init(autoreset=True, convert=True)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
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

    def insert_position(self, value, position):
        new_node = Node(value)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for _ in range(position - 1):
            if current is None:
                raise IndexError("Invalid position.")
            current = current.next

        if current is None:
            raise IndexError("Invalid position.")

        new_node.next = current.next
        current.next = new_node

    def delete_value(self, value):
        current = self.head

        if current is not None and current.value == value:
            self.head = current.next
            return

        previous = None

        while current is not None:
            if current.value == value:
                break
            previous = current
            current = current.next

        if current is None:
            print(Fore.YELLOW + "Value not found.")
            return

        previous.next = current.next

    def delete_index(self, position):
        if self.head is None:
            print(Fore.YELLOW + "List is empty.")
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head

        for _ in range(position - 1):
            if current is None or current.next is None:
                raise IndexError("Invalid index.")
            current = current.next

        if current.next is None:
            raise IndexError("Invalid index.")

        current.next = current.next.next

    def traverse(self):
        if self.head is None:
            print(Fore.RED + "Linked List is empty.")
            return

        print(Fore.GREEN + "Linked List:")

        current = self.head

        while current:
            print(current.value, end=" -> ")
            current = current.next

        print("None")


def display_menu():
    print("\n" + Style.BRIGHT + "===== Singly Linked List Menu =====")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete by Value")
    print("5. Delete by Index")
    print("6. Traverse List")
    print("7. Exit")


def main():
    linked_list = SinglyLinkedList()

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
                value = int(input("Enter value to delete: "))
                linked_list.delete_value(value)
                print(Fore.RED + "Delete operation completed.")

            elif choice == 5:
                position = int(input("Enter index to delete: "))
                linked_list.delete_index(position)
                print(Fore.RED + "Node deleted successfully.")

            elif choice == 6:
                linked_list.traverse()

            elif choice == 7:
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
            

