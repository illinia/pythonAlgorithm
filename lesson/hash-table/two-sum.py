def two_sum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = 1

    for v in nums:
        needed_number = target - v
        if needed_number in memo and needed_number != v:
            return True
    return False


target = 14
assert two_sum([4,1,9,7,5,3,16], target) is True
assert two_sum([4,1,9,7], target) is False


