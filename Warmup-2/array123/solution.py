def array123(nums):
    if len(nums) < 3:
        return False
    index = 0
    index_1 = 1
    index_2 = 2
    while index_2 < len(nums):
        if abs(nums[index] - nums[index_1]) == 1 and abs(nums[index] - nums[index_2]) == 2:
            return True
        index += 1
        index_1 += 1
        index_2 += 1
    return False
