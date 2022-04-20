def compareVersions(a, b):
    #Write your code here
    # if a == b:
    #     return 0
    # if len(a) != len(b):
    #     return 1 if len(a) > len(b) else -1
    a = list(map(int, a.split(".")))
    b = list(map(int, b.split(".")))
    mx = max(len(a), len(b))
    diff = abs(len(a) - len(b))
    if mx == len(a):
        b += [0] * diff
    elif mx == len(b):
        a += [0] * diff
    for i in range(mx):
        #try:
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1
        else:
            continue
        # #except:
        # if len(a) > len(b):
        #     b.append(0)
    # a = sum(list(map(int, a.split("."))))
    # b = sum(list(map(int, b.split("."))))
    # if a > b: return 1
    # elif a < b: return -1
    return 0
for i in range(int(input())):
    print(compareVersions(input(), input()))