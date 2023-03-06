from collections import deque

def can_visit_all_rooms(rooms):
    visited = [False] * len(rooms)

    # set, dictionary

    # v 에 연결되어 있는 모든 vertex 에 방문한다.
    # def dfs(cur_v):
    #     visited[cur_v] = True
    #     for next_v in rooms[cur_v]:
    #         if not visited[next_v]:
    #             dfs(next_v)
    #
    # dfs(0)

    def bfs(v):
        queue = deque();
        queue.append(v)
        visited[v] = True
        while queue:
            cur_v = queue.popleft()
            for next_v in rooms[cur_v]:
                if not visited[next_v]:
                    queue.append(next_v)
                    visited[next_v] = True

    bfs(0)

    return all(visited)

    # if len(visited) == len(rooms):
    #     return True
    # else:
    #     return False
    # return visited


rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(can_visit_all_rooms(rooms))
