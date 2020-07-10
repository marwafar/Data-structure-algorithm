class MinHeap:
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
            if child<parent:
               self.heap_list[index]=parent
               self.heap_list[self.parent_index(index)]=child
            index=self.parent_index(index)

    def retrieve_min(self):
        if self.count==0:
            return None
        min=self.heap_list[1]
        self.heap_list[1]=self.heap_list[self.count]
        self.heap_list.pop()
        self.count-=1
        self.heapify_down()
        return min
    
    def heapify_down(self):
        index=1
        while self.left_child_index(index)<=self.count:
            small_child_index=self.get_smaller_child_index(index)
            parent=self.heap_list[index]
            child=self.heap_list[small_child_index]
            if child<parent:
                self.heap_list[index]=child
                self.heap_list[small_child_index]=parent
            index=small_child_index

    def get_smaller_child_index(self,index):
        if self.left_child_index(index)==self.count:
            return self.left_child_index(index)
        else:
            left_child=self.heap_list[self.left_child_index(index)]
            right_child=self.heap_list[self.right_child_index(index)]
            if left_child<right_child:
                return self.left_child_index(index)
            else:
               return self.right_child_index(index) 

#--------------
# TEST
#---------------
min_heap=MinHeap()
min_heap.add(4)
min_heap.add(10)
min_heap.add(1)
min_heap.add(3)
min_heap.add(22)
min_heap.add(20)
print(min_heap.heap_list)
print(min_heap.retrieve_min())
print(min_heap.heap_list)
print(min_heap.retrieve_min())
print(min_heap.heap_list)
