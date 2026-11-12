from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    root = Node("N")
    root.left = Node("A")
    root.right = Node("D")
    root.left.left = Node("E")
    root.left.right = Node("R")
    root.right.left = Node("A")
    return root


def bfs(root):
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def dfs(root):
    result = []
    stack = [root]
    while stack:
        current = stack.pop()
        result.append(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result


tree = build_tree()
print("BFS:", " - ".join(bfs(tree)))
print("DFS:", " - ".join(dfs(tree)))