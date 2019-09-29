def end_other(a, b):
  c = a.lower()
  d = b.lower()
  return c.endswith(d) or d.endswith(c)
