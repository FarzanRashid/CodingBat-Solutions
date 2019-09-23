def has22(nums):
  index = 0
  index2 = index + 1
  while index2 < len(nums):
    if nums[index] == 2:
      if nums[index] - nums[index2] == 0:
        return True
    index += 1
    index2 += 1
  return False
