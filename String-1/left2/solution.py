def left2(str):
  if len(str) == 2:
    return str
  first = str[:2]
  last =  str[2:]
  return last + first
