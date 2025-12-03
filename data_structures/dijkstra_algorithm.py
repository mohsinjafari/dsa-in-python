"""
dijkstra_algorithm.py
---------------------
Implementation of Dijkstra's algorithm to find the shortest paths
from a starting node to all other nodes in a weighted graph.

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
# Dijkstra's Algorithm
# ----------------------------
def dijkstra_algorithm(graph, start):
    """
    Compute shortest path distances from the start node to all other nodes
    using Dijkstra's algorithm.

    :param graph: dict where keys are node names and values are lists of
                  tuples (neighbor, weight)
    :param start: starting node for Dijkstra's algorithm
    :return: dict of shortest distances to each node
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Min-heap: (distance, node)
    queue = [(0, start)]

    while queue:
        current_distance, node = heapq.heappop(queue)

        # Skip if we already found a shorter path
        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    start_node = "kabul"
    distances = dijkstra_algorithm(graph, start_node)
    print(f"Shortest distances from {start_node}:")
    for node, dist in distances.items():
        print(f"{node}: {dist}")
