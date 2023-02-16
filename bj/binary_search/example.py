def binary_search(target, data):
    # 시작 인덱스 0, 마지막 인덱스 전체 길이 - 1
    start = 0
    end = len(data) - 1

    # 시작 인덱스가 마지막 인덱스보다 크면 종료
    while start <= end:

        # 시작과 끝 합을 2로 나눈 몫
        mid = (start + end) // 2

        # 중간 값이 타겟이랑 일치하면 해당 값 반환
        if data[mid] == target:
            return data[mid]
        # 타겟보다 작으면 시작 인덱스를 중간 값 + 1로 설정하고 다시 반복
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


target = 3
data = [i for i in range(1, 11)]
data.sort()

print(binary_search(target=target, data=data))


def binary_search_recursion(target, data, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return data[mid]
    elif data[mid] < target:
        return binary_search_recursion(target, data, mid + 1, end)
    else:
        return binary_search_recursion(target, data, start, mid - 1)


target = 3
data = [i for i in range(1, 11)]
data.sort()
start = 0
end = len(data) - 1

print(binary_search_recursion(target, data, start, end))