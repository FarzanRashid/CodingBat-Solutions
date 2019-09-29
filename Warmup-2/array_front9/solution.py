def array_front9(nums):
  lenth = len(nums)
  if lenth > 4:
    lenth = 4
  for i  in range(lenth):
    if nums[i] == 9:
      return True
  return False
