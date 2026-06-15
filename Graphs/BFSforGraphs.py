from collections import deque

# Number of nodes
n = 9

# Adjacency List
adj = [
    [],         # 0 (unused)
    [2, 8],     # 1
    [1, 3, 4],  # 2
    [2],        # 3
    [2, 5],     # 4
    [4, 6],     # 5
    [5, 7],     # 6
    [8, 6],     # 7
    [1, 7, 9],  # 8
    [8]         # 9
]

def bfs(n, adj, start):
    visited = [0] * (n + 1)
    queue = deque()
    result = []

    # Start node
    queue.append(start)
    visited[start] = 1

    while queue:
        current = queue.popleft()
        result.append(current)

        # Visit all neighbours
        for node in adj[current]:
            if visited[node] == 0:
                visited[node] = 1
                queue.append(node)

    return result

# Start BFS from node 1
print("BFS Traversal:", bfs(n, adj, 1))
# Output: BFS Traversal: [1, 2, 8, 3, 4, 9, 5, 6, 7]
