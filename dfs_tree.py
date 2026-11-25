class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def preorder(node, result):
    if node is None:
        return
    result.append(node.data)       # Root
    preorder(node.left, result)    # Left
    preorder(node.right, result)   # Right



def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)     # Left
    result.append(node.data)       # Root
    inorder(node.right, result)    # Right



def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)   # Left
    postorder(node.right, result)  # Right
    result.append(node.data)       # Root


def build_tree():
    """Build the tree for the name JERSY NADERA."""
    root = Node("J")

    root.left = Node("E")
    root.right = Node("R")

    root.left.left = Node("S")
    root.left.right = Node("Y")
    root.right.left = Node("N")
    root.right.right = Node("A")

    root.left.left.left = Node("D")
    root.left.left.right = Node("E")
    root.left.right.left = Node("R")
    root.left.right.right = Node("A")

    return root


def main():
    root = build_tree()

    pre, ino, post = [], [], []
    preorder(root, pre)
    inorder(root, ino)
    postorder(root, post)

    print("DFS Methods in Binary Tree - JERSY NADERA")
    print("-" * 45)
    print("Preorder  (Root -> Left -> Right):", " -> ".join(pre))
    print("Inorder   (Left -> Root -> Right):", " -> ".join(ino))
    print("Postorder (Left -> Right -> Root):", " -> ".join(post))


if __name__ == "__main__":
    main()