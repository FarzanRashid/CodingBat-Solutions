def pos_neg(a, b, negative):
  if negative == True:
    if a < 0 and b < 0:
      return True
    else:
      return False
  else:
    if a < 0 and b < 0:
      return False
    if a > 0 and b > 0:
      return False
    if a < 0 or b < 0:
      return True
