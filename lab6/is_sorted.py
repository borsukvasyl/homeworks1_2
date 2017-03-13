def is_sorted(lst):
    for n in range(len(lst)):
        if type(lst[n]) != int:
            return False
        if n != (len(lst) - 1) and lst[n] > lst[n + 1]:
            return False
    return True
