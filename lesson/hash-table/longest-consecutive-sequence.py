def longest_consecutive(nums):
    nums_dict = {x: True for x in nums}
    count = 0

    for num in nums_dict:
        if num - 1 not in nums_dict:
            next = num + 1
            tmp_count = 1
            while next in nums_dict:
                tmp_count += 1
                next = next + 1
            count = max(count, tmp_count)

    return count


assert longest_consecutive([6, 7, 100, 5, 4, 4]) == 4
