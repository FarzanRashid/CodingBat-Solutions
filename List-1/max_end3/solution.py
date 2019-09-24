def max_end3(nums):
  if nums[0] > nums[-1]:
    return [nums[0], nums[0], nums[0]]
  else:
    return [nums[-1], nums[-1], nums[-1]]
