def count_hi(str):
  count = 0
  index = 0
  index2 = 1
  while index2 < len(str):
    if str[index] == "h" and str[index2] == "i":
      count += 1
    index += 1
    index2 += 1
  return count
