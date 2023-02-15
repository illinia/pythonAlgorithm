# from collections import deque
#
#
# def bfs(root):
#     visited = []
#     if root is None:
#         return []
#     q = deque()
#     q.append(root)
#     while q:
#         cur_node = q.popleft()
#         visited.append(cur_node.value)
#
#         if cur_node.left:
#             q.append(cur_node.left)
#         if cur_node.right:
#             q.append(cur_node.right)
#     return visited
#
#
# bfs(root)
#

from collections import deque

def bfs(root):
    visited = []

    if not root:
        return []

    queue = deque()

    queue.append(root)

    while queue:
        current_node = queue.popleft()
        visited.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return visited