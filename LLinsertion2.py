#Inserting Node At Last
class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.node=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
                n.ref=new_node
LL1=LinkedList()
LL1.add_end(100)
LL1.print_LL()