import sys

N = int(sys.stdin.readline())


def self_call(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return self_call(n - 1) + self_call(n - 2)


dp_dict = dict()

dp_dict[1] = 1
dp_dict[2] = 1

global dp_count
dp_count = 0


def dp(n):
    global dp_count

    if n == 1 or n == 2:
        dp_count += 1
    if n > 3:
        for i in range(3, n + 1):
            dp_count += 1
            dp_dict[i] = dp_dict[i - 1] + dp_dict[i - 2]


dp(N)
print(str(self_call(N)) + ' ' + str(dp_count))
