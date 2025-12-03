"""
graph_routes_weighted.py
------------------------
A weighted graph implementation (using adjacency matrix) with utility functions to find:
- all_paths: list all possible weighted paths between two nodes
- shortest_path: find the shortest weighted path between two nodes
- find_cost: compute path cost using the adjacency matrix

Graph is created from a list of weighted routes (edges).

Author: Mohsin Jafari
GitHub: https://github.com/mohsinjafari
"""


# ----------------------------
# Graph Data (Weighted Routes)
# ----------------------------

routes_weighted = [
    ["kabul", "qandahar", 5],
    ["kabul", "Herat", 7],
    ["qandahar", "Herat", 3],
    ["Herat", "mazar-i-sharif", 4],
    ["qandahar", "mazar-i-sharif", 6],
    ["mazar-i-sharif", "Farah", 8],
]


# ----------------------------
# Graph Construction
# ----------------------------

# Extract all unique nodes (sorted for consistent indexing)
nodes = sorted({node for s, e, _ in routes_weighted for node in (s, e)})

# Build adjacency list (unweighted connectivity)
graph = {}
for start, end, _ in routes_weighted:
    graph.setdefault(start, []).append(end)
    graph.setdefault(end, []).append(start)

# Build adjacency matrix (for weighted cost lookup)
adjacency_matrix = [[0] * len(nodes) for _ in range(len(nodes))]

for start, end, cost in routes_weighted:
    i, j = nodes.index(start), nodes.index(end)
    adjacency_matrix[i][j] = cost
    adjacency_matrix[j][i] = cost  # undirected graph


# ----------------------------
# Utility Functions
# ----------------------------

def find_cost(path):
    """
    Return total weight for a given path using adjacency matrix.
    """
    total = 0
    for i in range(len(path) - 1):
        s_i, e_i = nodes.index(path[i]), nodes.index(path[i + 1])
        total += adjacency_matrix[s_i][e_i]
    return total



def all_paths(graph, start, end):
    """
    Return all possible weighted paths between start and end nodes.
    Each result is stored as: [node1, node2, ..., nodeN, total_cost]
    """
    paths = []

    def inner(s, e, path):
        path = path + [s]

        if s == e:
            cost = find_cost(path)
            paths.append(path + [cost])
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
    Return the shortest weighted path between start and end using DFS.
    The result is: [node1, node2, ..., nodeN, total_cost]
    """
    shortest = None

    def inner(s, e, path):
        nonlocal shortest
        path = path + [s]

        if s == e:
            cost = find_cost(path)
            if shortest is None or cost < shortest[-1]:
                shortest = path + [cost]
            return

        if s not in graph:
            return

        for neighbor in graph[s]:
            if neighbor not in path:
                inner(neighbor, e, path)

    inner(start, end, [])
    return shortest



# ----------------------------
# Example usage (for testing)
# ----------------------------
if __name__ == "__main__":

    print("All weighted paths (kabul → mazar-i-sharif):")
    print(all_paths(graph, "kabul", "mazar-i-sharif"))

    print("\nShortest weighted path (kabul → mazar-i-sharif):")
    print(shortest_path(graph, "kabul", "mazar-i-sharif"))
