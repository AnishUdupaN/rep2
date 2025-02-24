class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def print_list(self):
        current=self.head
        while current:
            print(current.data,end="  ")
            current=current.next
        print()
def compare(self,list2):
    current1=self.head
    while current1:
        current2=list2.head
        while current2:
            if current1.data==current2.data:
                temp1=current1
                temp2=current2
                while temp1 and temp2 and temp1.data==temp2.data:
                    temp1=temp1.next
                    temp2=temp2.next
                if temp1 is None and temp2 is None:
                    print("TRUE")
                    return
                else:
                    break
            current2=current2.next
        current1=current1.next
    print("FALSE")
ll1=LinkedList()
ll2=LinkedList()
while True:
    print("1.add nodes to ll1\n2.add nodes to ll2\n3.compare ll1 and ll2\n4.Exit")
    choice=int(input("Enter choice : "))
    if choice==1:
        num=int(input("Enter value to add : "))
        ll1.add(num)
    elif choice==2:
        num=int(input("Enter value to add : "))
        ll2.add(num)
    elif choice==3:
        compare(ll1,ll2)
    elif choice==4:
        break
