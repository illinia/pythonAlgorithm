import sys

N = int(sys.stdin.readline())
move_list = []


def move(n, start, end):
  if (n == 0):
    return
  else:
    move(n - 1, start, 6 - start - end)
    move_list.append(str(start) + " " + str(end))
    move(n - 1, 6 - start - end, end)


move(N, 1, 3)

print(len(move_list))
print("\n".join(move_list))