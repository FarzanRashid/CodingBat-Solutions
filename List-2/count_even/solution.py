def count_evens(nums):
  output = 0
  for i in nums:
    if i % 2 == 0:
      output += 1
  return output
