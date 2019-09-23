def sum13(nums):
  output = 0
  index = 0
  while index < len(nums):
    if nums[index] == 13:
      index += 2 
      continue
    output += nums[index]
    index += 1
  return output
    
