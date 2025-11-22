def findAllPathsDfs(graph, start, end):

    def dfs(current, path, visited):
        
        path.append(current)
        visited.add(current)
        
        if current == end:
            allPaths.append(path.copy())
        else:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    dfs(neighbor, path, visited)
        
        path.pop()
        visited.remove(current)
        
    allPaths = []
    dfs(start, [], set())
    return allPaths

def main():
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2, 4],
        4: [3]
    }
    
    print("Graph: ", graph)
    print("\nEnter two vertices to find all paths between them:")
    
    try:
        startNode = int(input("Enter start vertex: "))
        endNode = int(input("Enter end vertex: "))
        
        if startNode not in graph or endNode not in graph:
            print("Error: One or both vertices not found in graph!")
            return
        
        paths = findAllPathsDfs(graph, startNode, endNode)
        
        if paths:
            print(f"\nYes, paths exist between {startNode} and {endNode}!")
            print(f"Number of paths found: {len(paths)}")
            print("Paths:")
            for i, path in enumerate(paths, 1):
                print(f" {i}. {path}")
        else :
            print(f"\nNo path exist between {startNode} and {endNode}")
            
    except ValueError:
        print("Error: Please enter valid integers!")

if __name__ == "__main__":
    main()