def make_tags(tag, word):
    first = "<" + tag + ">"
    last = "<" + "/" + tag + ">"
    return first + word + last
