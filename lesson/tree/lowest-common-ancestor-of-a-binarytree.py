class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lca(root, p, q):
    if root is None:
        return None

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if root.value == p or root.value == q:
        return root
    elif left and right:
        return root
    elif left or right:
        return left or right


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right = Node(1)
root.right.left = Node(0)
root.right.right = Node(8)

print(lca(root, 6, 4).value)
