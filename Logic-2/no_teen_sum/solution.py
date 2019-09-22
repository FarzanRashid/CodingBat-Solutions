def no_teen_sum(a, b, c):
    sum = 0
    sum += fix_teen(a)
    sum += fix_teen(b)
    sum += fix_teen(c)
    return sum


def fix_teen(n):
    if n == 15 or n == 16:
        return n
    elif n >= 13 and n <= 19:
        return 0
    else:
        return n
