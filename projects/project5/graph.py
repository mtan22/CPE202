//REMOVE

from typing import Any, List, Optional
from stack_array import * # Needed for Depth First Search
from queue_array import * # Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key: Any):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to: List = []
        self.visited = False
        self.color = None

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename: str):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.vert_dict: dict = {}
        self.vert_list: List = []
        try:
            with open(filename, "r") as file:
                for i in file:
                    vertices = i.split()
                    for j in vertices:
                        self.add_vertex(j)
                try:
                    self.add_edge(vertices[0], vertices[1])
                except:
                    raise IndexError
                file.close()
            if not file.close():
                file.close()
        except:
            raise FileNotFoundError("The file does not exist")

    def add_vertex(self, key: Any) -> None:
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        val = self.vert_dict.get(key)
        if val is None:
            vertex = Vertex(key)
            self.vert_dict[key] = vertex
            self.vert_list.append(key)

    def get_vertex(self, key: Any) -> Optional[Vertex]:
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        val = self.vert_dict.get(key)
        if val is None:
            return None
        return val

    def add_edge(self, v1: Any, v2: Any) -> None:
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.vert_dict[v1].adjacent_to.append(v2)
        self.vert_dict[v2].adjacent_to.append(v1)

    def get_vertices(self) -> List:
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        return sorted(self.vert_list)

    def conn_components(self) -> List:
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        component: List = []
        visited_list: List = []
        for i in self.vert_list:
            if i not in visited_list:
                con = self.dfs([], i, visited_list)
                component.append(con)
        return component

    def dfs(self, con: List[Any], key: Any, visit_list: List[Any]) -> List:
        og_stack = Stack(len(self.vert_list))
        og_stack.push(key)
        visit_list.append(key)
        while og_stack.is_empty() != True:
            pop_idx = og_stack.pop()
            if pop_idx not in con:
                con.append(pop_idx)
            else:
                pass
            for i in self.vert_list[pop_idx].adjacent_to:
                if i in con:
                    continue
                og_stack.push(i)
                visit_list.append(i)
        con.sort()
        return con

    def is_bipartite(self) -> bool:
        '''Returns True if the graph is bicolorable and False otherwise.
        This method MUST use Breadth First Search logic!'''
        queue = Queue(len(self.vert_list))
        for i in self.vert_list:
            if self.vert_list[i].color == "black":
                self.vert_list[i].color = "red"
                queue.enqueue(i)
            while queue.is_empty() is not True:
                idx = queue.dequeue()
                for j in self.vert_list[idx].adjacent_to:
                    if self.vert_list[j].color != "black":
                        if self.vert_list[j].color == self.vert_list[idx].color:
                            return False
                    else:
                        if self.vert_list[idx].color != "red":
                            self.vert_list[j].color = "red"
                            queue.enqueue(j)
                        else:
                            self.vert_list[j].color = "white"
                            queue.enqueue(j)
        return True
