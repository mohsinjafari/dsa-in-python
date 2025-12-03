"""
graph_routes_weighted.py
------------------------
A weighted graph implementation with Prim's algorithm to find
the Minimum Spanning Tree (MST) of a weighted undirected graph.

Author: Mohsin Jafari
GitHub: https://github.com/mohsinjafari
"""

import heapq

# ----------------------------
# Weighted graph data
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
# Graph construction
# ----------------------------
graph = {}
for start, end, cost in routes_weighted:
    graph.setdefault(start, []).append((end, cost))
    graph.setdefault(end, []).append((start, cost))


# ----------------------------
# Prim's Algorithm
# ----------------------------
def prims_algorithm(graph, start):
    """
    Implement Prim's algorithm to find the Minimum Spanning Tree (MST)
    of a weighted undirected graph.

    :param graph: dict with keys as node names and values as lists of
                  tuples (neighbor, weight)
    :param start: starting node for Prim's algorithm
    :return: total_cost (int), mst_edges (list of tuples (from, to, weight))
    """
    visited = set()
    mst_edges = []
    total_cost = 0

    # Min-heap: (weight, from_node, to_node)
    queue = [(0, None, start)]

    while queue:
        weight, frm, to = heapq.heappop(queue)
        if to in visited:
            continue

        visited.add(to)
        total_cost += weight
        if frm is not None:
            mst_edges.append((frm, to, weight))

        for neighbor, w in graph[to]:
            if neighbor not in visited:
                heapq.heappush(queue, (w, to, neighbor))

    return total_cost, mst_edges


# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    total_cost, mst_edges = prims_algorithm(graph, "kabul")
    print("Minimum Spanning Tree edges:", mst_edges)
    print("Total cost of MST:", total_cost)
    