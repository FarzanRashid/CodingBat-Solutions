def make_bricks(small, big, goal):
  if big * 5 + small < goal:
    return False
  elif goal < big * 5:
    if small < goal % 5:
      return False
    else:
      return True
  else:
    return True
      
