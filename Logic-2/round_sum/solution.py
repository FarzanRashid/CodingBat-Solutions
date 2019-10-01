def helper(a):
    last_digit = a % 10
    if last_digit < 5:
        return a - last_digit
    else:
        return a +  (10 - last_digit)


def round_sum(a, b, c):
    return helper(a) + helper(b) + helper(c)
