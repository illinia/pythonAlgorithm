from collections import deque


def shortest_path_binary_matrix(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])

    if grid[0][0] == 1 or grid[row-1][col-1] == 1:
        return shortest_path_len

    delta = [(1, 0), (-1, 0), (0, 1), (0, -1),
             (1, 1), (1, -1), (-1, 1), (-1, -1)]

    visited = [[False] * col for _ in range(row)]
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        # 목적지에 도착했을 때 cur_len를 shortest_path_len 에 저장하면 된다.
        if cur_r == row - 1 and cur_c == col - 1:
            shortest_path_len = cur_len
            break

        # 연결되어있는 노드들 확인하기
        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < row and 0 <= next_c < col:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len + 1))
                    visited[next_r][next_c] = True

    return shortest_path_len

print(shortest_path_binary_matrix(grid=[
    [0,0,0],
    [1,1,0],
    [1,1,0]
]))