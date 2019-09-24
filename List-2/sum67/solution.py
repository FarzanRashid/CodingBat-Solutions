def sum67(nums):
    output = 0
    index = 0
    while index < len(nums):
        if nums[index] == 6:
            while nums[index] != 7:
                index += 1
        else:
            output += nums[index]
        index += 1
    return output
