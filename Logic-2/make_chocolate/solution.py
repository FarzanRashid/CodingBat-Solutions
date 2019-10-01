def make_chocolate(small, big, goal):
  if small + big * 5 < goal:
    return -1
  elif big * 5 > goal:
    if small < goal % 5:
      return -1 
    else:
      return goal % 5
  else:
    return goal - big * 5
