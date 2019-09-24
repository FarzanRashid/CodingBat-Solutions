def string_bits(str):
  output = ''
  index2 = 0
  while index2 < len(str):
    output += str[index2]
    index2 += 2
  return output
    
