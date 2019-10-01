def string_splosion(str):
  output = ""
  for i in range(len(str)):
    output += str[:i+1]
  return output
