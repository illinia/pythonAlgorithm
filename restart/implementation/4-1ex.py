# n = int(input())
#
# data = list(input().split())
#
# location = [1,1]
#
# for i in data:
#     if i == 'R' and location[1] < n:
#         location[1] += 1
#     elif i == 'L' and location[1] > 1:
#         location[1] -= 1
#     elif i == "U" and location[0] > 1:
#         location[0] -= 1
#     elif i == "D" and location[0] < n:
#         location[0] += 1
#
# print(location[0], location[1])

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

# 5
# R R R U D D