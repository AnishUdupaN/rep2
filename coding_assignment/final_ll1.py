class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printit(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end="  ")
            current = current.next
        print()

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Node with value {data} added at the front.")

    def insert_at_rear(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Node with value {data} added at the rear.")
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        print(f"Node with value {data} added at the rear.")

    def delete_at_front(self):
        if self.head is None:
            print("The list is empty. No nodes to remove.")
            return
        self.head = self.head.next
        print("Node at the front has been removed.")

    def delete_at_rear(self):
        if self.head is None:
            print("The list is empty. No nodes to remove.")
            return
        if self.head.next is None:
            self.head = None
            print("Node at the rear has been removed.")
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None
        print("Node at the rear has been removed.")

    def insert_at_pos(self, pos, data):
        new_node = Node(data)
        if pos < 0:
            print("Invalid position.")
            return
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            print(f"Node with value {data} added at position {pos}.")
            return
        current = self.head
        count = 0
        while current and count < pos - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of bounds.")
            return
        new_node.next = current.next
        current.next = new_node
        print(f"Node with value {data} added at position {pos}.")

    def delete_at_pos(self, pos):
        if pos < 0:
            print("Invalid position.")
            return
        current = self.head
        if current is None:
            print("The list is empty. No nodes to remove.")
            return
        if pos == 0:
            self.head = current.next
            print("Node at position 0 has been removed.")
            return
        count = 0
        prev = None
        while current and count < pos:
            prev = current
            current = current.next
            count += 1
        if current is None:
            print("Position out of bounds.")
            return
        prev.next = current.next
        print(f"Node at position {pos} has been removed.")


ll = LinkedList()
while True:
    print("\nMenu:")
    print("1. Insert at front")
    print("2. Insert at rear")
    print("3. Delete at front")
    print("4. Delete at rear")
    print("5. Insert at position")
    print("6. Delete at position")
    print("7. Print linked list")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter the value of the node to be added at the front: "))
        ll.insert_at_front(val)
    elif choice == 2:
        val = int(input("Enter the value of the node to be added at the rear: "))
        ll.insert_at_rear(val)
    elif choice == 3:
        ll.delete_at_front()
    elif choice == 4:
        ll.delete_at_rear()
    elif choice == 5:
        pos = int(input("Enter the position: "))
        val = int(input("Enter the value of the node to be added: "))
        ll.insert_at_pos(pos, val)
    elif choice == 6:
        pos = int(input("Enter the position of the node to be deleted: "))
        ll.delete_at_pos(pos)
    elif choice == 7:
        ll.printit()
    elif choice == 8:
        break
    else:
        print("Invalid choice. Please try again.")
