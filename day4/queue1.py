#inserting at front and deleting at end


import sys


class Queue:
    def __init__(self, size=5):
        self.que = []
        self.size = size
        print("Empty Queue is created")
    def insert_front(self):
        if len(self.que) == self.size:
            print("Queue is full")
        else:
            element = input("Enter the element to be inserted: ")
            self.que.insert(0, element)
    def insert_rear(self):
        if len(self.que) == self.size:
            print("Queue is full")
        else:
            element = input("Enter the element to be inserted: ")
            self.que.append(element)
    def delete_front(self):
        if not self.que:
            print("Queue is empty")
        else:
            print(f"Popped element is {self.que.pop(0)}")
    def delete_rear(self):
        if not self.que:
            print("Queue is empty")
        else:
            print(f"Popped element is {self.que.pop()}")
            
    def list_queue(self):
        if not self.que:
            print("Queue is empty")
        else :
            print("The Queue elements: ", self.que)


class Menu:
    def __init__(self): 
        pass
    def get_menu(self, queue):
        menu = {
            1 : queue.insert_front,
            2 : queue.insert_rear,
            3 : queue.delete_front,
            4 : queue.delete_rear,
            5 : queue.list_queue,
            6 : self.end_of_program
        }
        return menu
    def end_of_program(self):
        sys.exit("Exit")
    def invalid_choice(self):
        print("Invalid choice")
    def run_menu(self):
        queue = Queue()
        while(True):
            choice = int(input("1.Insert Front\n2.Insert Rear\n3.Delete Front\n4.Delete Rear\n5.Display,-1.To Exit: "))
            if choice == -1 :
                break
            menu = self.get_menu(queue)
            menu.get(choice, self.invalid_choice)()
        print("End of Program")


menu = Menu()
menu.run_menu()