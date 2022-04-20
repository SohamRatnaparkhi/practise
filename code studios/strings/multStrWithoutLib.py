def multiplyStrings(a, b):
    # Write your code here
    sm = 0
    b = list(b)
    a = list(a)
    b.reverse()
    a.reverse()
    h = 0
    for i in range(len(b)):
        x = ord(b[i]) - 48
        s = 0
        for j in range(len(a)):
            y = ord(a[j]) - 48
            l = x * y
            s += l * (10 ** j)
        sm += s * (10 ** h)
        h += 1
    return sm
    # Return the product of both given numbers
    pass
for i in range(int(input())):
    print(multiplyStrings(input(), input()))