def is_isogram(string):
    if not string:
        return True
    lower_str = string.lower()
    for s in lower_str:
        if ord(s) in range(97,123):
            if lower_str.count(s) > 1:
                return False
    return True









