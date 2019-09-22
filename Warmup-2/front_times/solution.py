def front_times(str, n):
    if len(str) < 3:
        return str * n
    else:
        return (str[0] + str[1] + str[2]) * n


