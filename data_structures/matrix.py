"""
matrix.py
------------------------
Implement various matrix traversal and path-finding algorithms including:
- Row-wise and Column-wise traversal
- BFS traversal from a cell
- All paths in a binary matrix
- Shortest path in a binary matrix
- Dijkstra's algorithm for weighted matrices

Author: Mohsin Jafari
GitHub: https://github.com/mohsinjafari
"""

from collections import deque
import heapq

# ----------------------------
# Row-wise traversal
# ----------------------------
def row_wise_traversal(matrix):
    result = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            result.append(matrix[i][j])
    return result


# ----------------------------
# Column-wise traversal
# ----------------------------
def column_wise_traversal(matrix):
    result = []
    rows = len(matrix)
    cols = len(matrix[0])
    for col in range(cols):
        for row in range(rows):
            result.append(matrix[row][col])
    return result


# ----------------------------
# BFS traversal from a cell
# ----------------------------
def BFS_Traversal(matrix, row, col):
    result = []
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    queue = deque()
    queue.append((row, col))

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        result.append(matrix[x][y])

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                queue.append((nx, ny))

    return result


# ----------------------------
# Find all paths in a binary matrix
# ----------------------------
def all_paths_binary_matrix(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0])
    paths = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    que = deque()
    que.append([*start, [start]])

    while que:
        x, y, path = que.popleft()
        if [x, y] == end:
            paths.append(path)
            continue

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 0 and [nx, ny] not in path:
                que.append([nx, ny, path + [[nx, ny]]])

    return paths


# ----------------------------
# Shortest path in a binary matrix
# ----------------------------
def shortest_path_binary_matrix(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    que = deque()
    que.append([*start, [start]])

    while que:
        x, y, path = que.popleft()
        if [x, y] == end:
            return path

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 0 and [nx, ny] not in path:
                que.append([nx, ny, path + [[nx, ny]]])

    return -1


# ----------------------------
# Dijkstra's algorithm for weighted matrix
# ----------------------------
def dijkstra_algorithm(matrix, start):
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0

    min_heap = [(0, start[0], start[1])]

    while min_heap:
        current_dist, x, y = heapq.heappop(min_heap)

        if current_dist > dist[x][y]:
            continue

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_dist = current_dist + matrix[nx][ny]
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(min_heap, (new_dist, nx, ny))

    return dist


# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    binary_matrix = [
        [0, 0, 1],
        [0, 0, 0],
        [1, 0, 0]
    ]

    weighted_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Row-wise traversal:", row_wise_traversal(binary_matrix))
    print("Column-wise traversal:", column_wise_traversal(binary_matrix))
    print("BFS from (0,0):", BFS_Traversal(binary_matrix, 0, 0))
    print("All paths from [0,0] to [2,2]:", all_paths_binary_matrix(binary_matrix, [0, 0], [2, 2]))
    print("Shortest path from [0,0] to [2,2]:", shortest_path_binary_matrix(binary_matrix, [0, 0], [2, 2]))
    print("Dijkstra distance matrix from (0,0):")
    dist_matrix = dijkstra_algorithm(weighted_matrix, (0, 0))
    for row in dist_matrix:
        print(row)
