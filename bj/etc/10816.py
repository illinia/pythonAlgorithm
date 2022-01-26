from bisect import bisect_left, bisect_right

n = int(input())
n_num = sorted(list(map(int, input().split())))

m = int(input())
m_num = list(map(int, input().split()))
#
# dic = dict()
#
# for i in n_num:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
#
#
# for i in range(m):
#     if m_num[i] in dic:
#         print(dic[m_num[i]], end=' ')
#     else:
#         print(0, end=' ')


def count_by_range(a, value):
    right_index = bisect_right(a, value)
    left_index = bisect_left(a, value)
    return right_index-left_index


for i in range(m):
    print(count_by_range(n_num, m_num[i]), end=' ')