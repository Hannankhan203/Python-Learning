from collections import deque

def bfsShortestPath(graph, start, target):
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        currentVertex, path = queue.popleft()
        
        if currentVertex == target:
            return path
        
        for neighbor in graph[currentVertex]:
            if neighbor is not visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H'],
    'F': ['C', 'G'],
    'G': ['D', 'F', 'H'],
    'H': ['E', 'G']
}

start = 'A'
target = 'F'
shortestPath = bfsShortestPath(graph, start, target)

if shortestPath:
    print(f"Shortest path from {start} to {target}: {' -> '.join(shortestPath)}")
    print(f"Distance: {len(shortestPath) - 1}")
else:
    print(f"No path found from {start} to {target}")