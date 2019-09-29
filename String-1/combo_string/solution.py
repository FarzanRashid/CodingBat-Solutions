def combo_string(a, b):
    lenth_a = len(a)
    lenth_b = len(b)
    if lenth_a > lenth_b:
        return b + a + b
    else: 
        return a + b + a
    
