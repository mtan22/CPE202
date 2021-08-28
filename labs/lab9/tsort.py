from typing import Dict

from stack_array import *

class vertex:
    def __init__(self, adjacencies: List):
        self.in_degree = 0
        self.adjacencies = adjacencies

def tsort(vertices: List) -> str:
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    elif len(vertices) % 2 != 0:
        raise ValueError("input contains an odd number of tokens")
    else:
        sol = ""
        dict = adjacency_dict(vertices)
        stack = Stack(len(vertices))
        for i in dict:
            if dict[i].in_degree == 0:
                stack.push(i)
        if stack.is_empty() == True:
            raise ValueError("input contains a cycle")
        while stack.is_empty() == False:
            popped = stack.pop()
            sol += popped + "\n"
            for i in dict[popped].adjacencies:
                dict[i].in_degree -= 1
                if dict[i].in_degree == 0:
                    stack.push(i)
        return sol

def adjacency_dict(vertices: List) -> dict:
    dict_of_vertices: Dict[Any, Any] = {}
    for i in range(0, len(vertices), 2):
        if vertices[i] in dict_of_vertices:
            dict_of_vertices[vertices[i]].adjacencies += [vertices[i+1]]
        else:
            dict_of_vertices[vertices[i]] = vertex([vertices[i+1]])
        if vertices[i + 1] in dict_of_vertices:
            dict_of_vertices[vertices[i+1]].in_degree += 1
        else:
            dict_of_vertices[vertices[i+1]] = vertex([])
            dict_of_vertices[vertices[i+1]].in_degree += 1
    return dict_of_vertices
