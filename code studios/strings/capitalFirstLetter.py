def convertString(str):
    # Write your code here
    str = list(str)
    str[0] = str[0].upper()
    for i in range(len(str) - 1):
        if str[i] == " ":
            str[i + 1] = str[i + 1].upper()
    return "".join(str)

print(convertString("they are playing cricket"))