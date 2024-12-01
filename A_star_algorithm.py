def a_star(graph, start, goal, heuristic):
    open_set = {start}  # Nodes to explore
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0  # Cost to start is 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    came_from = {}  # To track the path

    while open_set:
        # Find the node in open_set with the lowest f_score
        current = min(open_set, key=lambda node: f_score[node])
        if current == goal:  # Goal reached
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return the path

        open_set.remove(current)
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                open_set.add(neighbor)

    return None  # No path found

# Example graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic (estimated cost to reach the goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 3,
    'E': 2,
    'F': 0
}

# Run A* from 'A' to 'F'
path = a_star(graph, 'A', 'F', heuristic)
print("Path:", path)
