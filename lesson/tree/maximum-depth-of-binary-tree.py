# level order 방식 풀이
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = Node(value=3)
root.left = Node(value=9)
root.right = Node(value=20)
root.right.left = Node(value=15)
root.right.right = Node(value=7)


def bfs(root):
    if not root:
        return 0

    max_depth = 0
    q = deque()
    q.append((root, 1))

    while q:
        current_node, current_depth = q.popleft()
        max_depth = current_depth

        if current_node.left:
            q.append((current_node.left, current_depth + 1))
        if current_node.right:
            q.append((current_node.right, current_depth + 1))

    return max_depth


print(bfs(root))


def max_depth(root):
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right) + 1


print(max_depth(root))
