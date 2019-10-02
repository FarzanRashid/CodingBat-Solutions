def string_match(a, b):
  output = 0
  index = 0
  index_1 = 1
  while index_1 < len(a) and index_1 < len(b):
    if a[index] == b[index] and a[index_1] == b[index_1]:
      output += 1
    index += 1
    index_1 += 1
  return output
