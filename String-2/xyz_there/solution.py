def xyz_there(str):
  index = 0
  index_2 = 1
  index_3 = 2
  while index_3 < len(str):
    if str[index] == "x" and str[index-1] != ".":
      if str[index_2] == "y" and str[index_3] == "z":
        return True
    index += 1
    index_2 += 1
    index_3 += 1
  return False
