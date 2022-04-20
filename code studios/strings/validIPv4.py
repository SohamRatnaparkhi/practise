def isValidIPv4(s):
    # Write your code here.
    try:
        a = list(map(int, s.split('.')))
    except:
        return False
    if len(a) != 4:
        return False
    for i in a:
        if i < 0 or i > 255:
            return False
    return True
    pass
print(isValidIPv4(input()))