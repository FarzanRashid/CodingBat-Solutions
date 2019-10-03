def count_code(str):
  output = 0
  for  i in range(len(str)):
    if str[i:i+2] == "co" and str[i+3:i+4] == "e":
      output += 1
  return output
