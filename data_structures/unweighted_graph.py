
"""
graph_routes.py
----------------
A simple graph implementation with utility functions to find:
- all_paths: list all possible paths between two nodes
- shortest_path: find the shortest path between two nodes
- BFS_Traversal: breadth-first search traversal
- DFS_Traversal: depth-first search traversal

Graph is created from a list of routes (edges).

Author: Mohsin Jafari
GitHub: https://github.com/mohsinjafari
"""

# ----------------------------
# Graph Data (Routes)
# ----------------------------

routes = [
    ["kabul", "qandahar"],
    ["kabul", "Herat"],
    ["qandahar", "Herat"],
    ["Herat", "mazar-i-sharif"],
    ["qandahar", "mazar-i-sharif"],
    ["mazar-i-sharif", "Farah"],
]


# ----------------------------
# Graph Construction
# ----------------------------

graph = {}

for start, end in routes:
    # Add edge start -> end
    if start not in graph:
        graph[start] = [end]
    else:
        graph[start].append(end)

    # Add edge end -> start (undirected graph)
    if end not in graph:
        graph[end] = [start]
    else:
        graph[end].append(start)


# ----------------------------
# Utility Functions
# ----------------------------

def all_paths(graph, start, end):
    """
    Return all possible paths between start and end nodes.
    """
    paths = []

    def inner(s, e, path):
        path = path + [s]

        if s == e:
            paths.append(path)
            return

        if s not in graph:
            return

        for neighbor in graph[s]:
            if neighbor not in path:
                inner(neighbor, e, path)

    inner(start, end, [])
    return paths



def shortest_path(graph, start, end):
    """
    Return the shortest path between start and end using DFS.
    """
    shortest = None

    def inner(s, e, path):
        nonlocal shortest
        path = path + [s]

        if s == e:
            if shortest is None or len(path) < len(shortest):
                shortest = path
            return

        if s not in graph:
            return

        for neighbor in graph[s]:
            if neighbor not in path:
                inner(neighbor, e, path)

    inner(start, end, [])
    return shortest



def BFS_Traversal(graph, start):
    """
    Print BFS traversal order starting from node 'start'.
    """
    queue = [start]
    visited = set()

    while queue:
        node = queue.pop(0)
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)



def DFS_Traversal(graph, start):
    """
    Print DFS traversal order starting from node 'start'.
    """
    stack = [start]
    visited = set()

    while stack:
        node = stack[-1]

        if node not in visited:
            print(node)
            visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)
                break
        else:
            stack.pop()



# ----------------------------
# Example usage (for testing)
# ----------------------------
if __name__ == "__main__":
    print("All paths (kabul → mazar-i-sharif):")
    print(all_paths(graph, "kabul", "mazar-i-sharif"))

    print("\nShortest path (kabul → mazar-i-sharif):")
    print(shortest_path(graph, "kabul", "mazar-i-sharif"))

    print("\nBFS Traversal from 'kabul':")
    BFS_Traversal(graph, "kabul")

    print("\nDFS Traversal from 'kabul':")
    DFS_Traversal(graph, "kabul")