class MaxHeap():
    def __init__(self):
        self.count=0
        self.heap_list=[None]
    
    def parent_index(self,idx):
        return idx//2
    def left_child_index(self,idx):
        return idx*2
    def right_child_index(self,idx):
        return idx*2+1
    
    def add(self,element):
        self.count+=1
        self.heap_list.append(element)
        self.heapify_up()
    
    def heapify_up(self):
        index=self.count
        while self.parent_index(index)>0:
            child=self.heap_list[index]
            parent=self.heap_list[self.parent_index(index)]
            if child>parent:
                self.heap_list[index]=parent
                self.heap_list[self.parent_index(index)]=child
            index=self.parent_index(index)
    
    def retrieve_max(self):
        max=self.heap_list[1]
        self.heap_list[1]=self.heap_list[self.count]
        self.count-=1
        self.heap_list.pop()
        self.heapify_down()
        return max
    
    def heapify_down(self):
        index=1
        while self.left_child_index(index)<=self.count:
            larger_child_index=self.get_larger_child_index(index)
            child=self.heap_list[larger_child_index]
            parent=self.heap_list[index]
            if parent<child:
                self.heap_list[index]=child
                self.heap_list[larger_child_index]=parent
            index=larger_child_index

    def get_larger_child_index(self,index):
        if self.left_child_index(index)==self.count:
            return self.left_child_index(index)
        else:
            left_child=self.heap_list[self.left_child_index(index)]
            right_child=self.heap_list[self.right_child_index(index)]
            if left_child>right_child:
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)

#---------------
# Test
# --------------
max_heap=MaxHeap()
max_heap.add(3)
max_heap.add(10)
max_heap.add(90)
max_heap.add(4)
max_heap.add(30)
max_heap.add(5)
max_heap.add(100)
max_heap.add(80)
print(max_heap.heap_list)  
print(max_heap.retrieve_max())  
print(max_heap.heap_list)
print(max_heap.retrieve_max())  
print(max_heap.heap_list)
