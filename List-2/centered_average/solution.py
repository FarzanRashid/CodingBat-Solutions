def centered_average(nums):
  nums.sort()
  output = 0
  index = 1
  while index <= len(nums) -1:
    if index == len(nums) - 1:
      break
    output += nums[index]
    index += 1
  return output // (len(nums) -2)
