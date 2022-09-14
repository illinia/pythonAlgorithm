input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, -2), (1, 2)]

count = 0

for step in steps:
    moved_data = (row + step[0], column + step[1])
    if moved_data[0] >= 1 and moved_data[0] <= 8 and moved_data[1] >= 1 and moved_data[1] <= 8:
        count += 1

print(count)
