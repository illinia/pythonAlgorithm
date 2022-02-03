n = int(input())

for _ in range(n):
    i = int(input())

    zero_list = [1, 0]
    one_list = [0, 1]

    if i > 1:
        for _ in range(i - 1):
            zero_list.append(zero_list[-1] + zero_list[-2])
            one_list.append(one_list[-1] + one_list[-2])

    print(zero_list[i], one_list[i])