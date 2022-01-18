n = int(input())
#
# datas = input().split()
#
# coord = [1, 1]
#
# for data in datas:
#     if data == 'L':
#         coord[1] -= 1
#     elif data == 'R':
#         coord[1] += 1
#     elif data == 'U':
#         coord[0] -= 1
#     elif data == 'D':
#         coord[0] += 1
#
#     if coord[0] < 1: coord[0] = 1
#     if coord[1] < 1: coord[1] = 1
#
# print(coord[0], ' ', coord[1])
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)