def isSubSequence(str2, str1):
    i, j = 0, 0
    while i < len(str1):
        if str2[j] == str1[i]:
            i += 1
            j += 1
        else:
            i += 1
        
    return j == len(str2)
    pass
tc = int(input())
while tc:
    print(isSubSequence(input(), input()))
    tc -= 1
