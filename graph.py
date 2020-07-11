# Build Vertex class
class Vertex:
    def __init__(self,value):
        self.value=value
        self.edges={}
    
    def add_edges(self,vertex,weight=0):
        self.edges[vertex]=weight
    
    def get_edges(self):
        return list(self.edges.keys())
#----------------------------------------
# Build the graph
class Graph:
    def __init__(self,directed=False):
        self.directed=directed
        self.graph_dict={}
    
    def add_vertex(self,vertex):
        self.graph_dict[vertex.value]=vertex
    
    def add_edges(self,from_vertex,to_vertex,weight=0):
        self.graph_dict[from_vertex.value].add_edges(to_vertex.value)
        if self.directed:
           self.graph_dict[to_vertex.value].add_edges(from_vertex.value)
    
    def find_path(self,start_vertex,end_vertex):
        seen={}
        path=[]
        start=[start_vertex.value]
        while len(start)>0:
            current_vertex=start.pop(0)
            seen[current_vertex]=True
            path+=[current_vertex]
            if current_vertex == end_vertex.value:
                return path
            else:
                vertices_to_visit=self.graph_dict[current_vertex].get_edges()
                start+=[vertex for vertex in vertices_to_visit if vertex not in seen]
        return "No path"
            
#----------------------
# TEST
#-----------------------
g=Graph(True)
a=Vertex('a')
b=Vertex('b')
c=Vertex('c')
d=Vertex('d')
e=Vertex('e')
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
#print(g.graph_dict.keys())
g.add_edges(a,b)
#g.add_edges(a,c)
g.add_edges(c,e)
#g.add_edges(e,d)
g.add_edges(d,b)
#print(a.edges)
print(g.find_path(d,e))


