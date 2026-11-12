from collections import deque

graph = {
    "N": ["A1", "D", "E"],
    "A1": ["N", "R"],
    "D": ["N", "A2"],
    "E": ["N", "A2"],
    "A2": ["D", "E"],
    "R": ["A1"],
}


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    result = []
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    visited.add(start)
    result.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    return result


def show(path):
    return " - ".join("A" if v.startswith("A") else v for v in path)


print("BFS:", show(bfs(graph, "N")))
print("DFS:", show(dfs(graph, "N")))