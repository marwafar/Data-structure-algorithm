class Node:
    def __init__(self,value):
        self.value=value
        self.next_node=None
    
    def get_value(self):
        return slef.value
    def get_next_node(self):
        return self.next_node

class LinkedList:
    def __init__(self):
        self.head_node=None
    
    def instert_at_begining(self,value):
        new_node=Node(value)
        new_node.next_node=self.head_node
        self.head_node=new_node
    
    def insert_at_end(self,value):
        new_node=Node(value)
        current_node=self.head_node
        if current_node is None:
            self.head_node=new_node
        else:
            while current_node:
                next=current_node.next_node
                if next is None:
                    current_node.next_node=new_node
                    break
                current_node=current_node.next_node
    
    def insert_after_node(self,value,prev_node):
        new_node=Node(value)
        current_node=self.head_node
        if current_node==prev_node:
            new_node.next_node=current_node.next_node
            current_node.next_node=new_node
        else:
            while current_node != prev_node:
                current_node=current_node.next_node
            new_node.next_node=current_node.next_node
            current_node.next_node=new_node

    def print_list(self):
        current_node=self.head_node
        if current_node is None:
            print("Empty list")
        else:
            while current_node:
                print(current_node.value)
                current_node=current_node.next_node
    

l=LinkedList()
l.instert_at_begining(3)
l.instert_at_begining(4)
l.instert_at_begining(15)
l.instert_at_begining(7)
l.instert_at_begining(10)
#print(l.head_node.value)
#l.print_list()
l.insert_at_end(28)
l.insert_at_end(30)
#l.print_list()
l.insert_after_node(55,l.head_node.next_node)
l.print_list()


