def bfs(graph, start):
    queue = [start]  # Queue to track nodes to visit
    visited = []  # List to track visited nodes

    while queue:
        node = queue.pop(0)  # Remove the first node from the queue
        if node not in visited:
            visited.append(node)  # Mark it as visited
            queue.extend(graph[node])  # Add its neighbors to the queue
    
    print("Visited nodes:", visited)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Run BFS starting from node 'A'
bfs(graph, 'A')
