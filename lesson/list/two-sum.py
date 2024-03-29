# 완전탐색
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False


# print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))

# 정렬, 포인터
def twoSum2(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] > target:
            r = r - 1
        elif nums[l] + nums[r] < target:
            l = l + 1
        elif nums[l] + nums[r] == target:
            return True
    return False

print(twoSum2(nums=[4, 1, 9, 7, 5, 3, 16], target=4))