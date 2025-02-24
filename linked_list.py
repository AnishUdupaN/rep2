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

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, data):
        current = self.head
        if current is None:
            print("The list is empty. No nodes to remove.")
            return

        if current.data == data:
            self.head = current.next
            print(f"Node with value {data} has been removed.")
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            print(f"Node with value {data} not found.")
            return
        prev.next = current.next
        print(f"Node with value {data} has been removed.")


ll = LinkedList()

while True:
    print("1.Add node\n2.Remove node\n3.Print linked list\n4.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        ll.add(int(input("Enter the value of the node to be added : ")))
    elif choice==2:
        ll.remove(int(input("Enter the value of Node to be deleted : ")))
    elif choice==3:
        ll.printit()
    elif choice==4:
        break



