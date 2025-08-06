"""
Depth-First Search (DFS) Algorithm for Graph Traversal

This function implements the Depth-First Search (DFS) algorithm, which is used to
traverse or search through a graph. DFS starts at a given vertex and explores
as far as possible along each branch before backtracking. This can be implemented 
either recursively or iteratively using a stack.

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.

Parameters:
G (Graph): The graph represented as an adjacency list.
v (int): The starting vertex for the DFS traversal.

-------------------------------
**Recursive DFS:**

The recursive approach uses the system's call stack to keep track of the vertices
to visit. The algorithm explores the graph by visiting the neighbors of each vertex
before backtracking.

Pseudocode:
visited = [False] * len(G)
def dfs(G, v):
    visit(v)                # Process the vertex v
    visited[v] = True        # Mark v as visited
    
    for w in G.neighbors(v): # For each neighbor w of v
        if not visited[w]:   # If w hasn't been visited
            dfs(G, w)        # Recursively visit w
            
-------------------------------
**Iterative DFS (Using Stack):**

The iterative version uses an explicit stack to simulate the systems call stack.
It avoids the limitations of recursion depth and is more flexible in handling 
very large graphs.

Pseudocode:
visited = []
def dfs(G, v):
    stack = [v]             # Start DFS from vertex v
    while stack:            # While the stack is not empty
        v = stack.pop()     # Pop the last vertex from the stack
        if v not in visited:  # If v hasn't been visited
            visited.append(v)  # Mark v as visited
            for w in G.neighbors(v):  # Visit all neighbors of v
                if w not in visited:  # If neighbor w hasn't been visited
                    stack.append(w)   # Push w onto the stack
                    
-------------------------------
**DFS Ordering:**

DFS can process vertices in two main orders depending on when the vertex is
added to the order list:

- **Pre-Order**: The vertex is added to the order **as soon as it is encountered**.
    This means the vertex is processed before its neighbors.

- **Post-Order**: The vertex is added to the order **only when there are no other explorable paths**.
    This means the vertex is processed after all its neighbors have been visited.

-------------------------------
**Time Complexity**:
- Time complexity is O(V + E), where:
    - V is the number of vertices
    - E is the number of edges
- This is because every vertex is visited once, and for each vertex, all its edges are checked.

**Space Complexity**:
- The space complexity depends on the implementation:
    - Recursive: O(V) for the call stack.
    - Iterative: O(V) for the stack and visited list.
"""

class GraphA:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since this is an undirected graph

    def dfs_recursive(self, v, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(v)  # Mark the vertex as visited
        print(v, end=" ")  # Print the visited vertex
        
        for neighbor in self.graph[v]:  # Visit all the neighbors
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

# Test case for Recursive DFS
graph = GraphA()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

print("Recursive DFS traversal starting from vertex 'A':")
graph.dfs_recursive('A')  # Expected output: A B D C


class GraphB:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since this is an undirected graph

    def dfs_iterative(self, start):
        visited = set()  # To keep track of visited nodes
        stack = [start]  # Stack to hold vertices
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")  # Print the visited vertex
                visited.add(vertex)
                # Push all unvisited neighbors to the stack
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)

# Test case for Iterative DFS
graph = GraphB()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

print("\nIterative DFS traversal starting from vertex 'A':")
graph.dfs_iterative('A')  # Expected output: A C D B
