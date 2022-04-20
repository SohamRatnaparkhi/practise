from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def kThCharaterOfDecryptedString(s, k) :
    num = "0"
    N = []
    x = ""
    X = ["#"]
    s = list(s)
    for i in range(0, len(s)):
        if ord(s[i]) > 47 and ord(s[i]) < 58:
            num += s[i]
        else:
            x += s[i]
        # N.append((num))
        # X.append(x)
        # a = ord(s[i + 1])

        if num != "0" and (i + 1 < len(s) - 1 and (ord(s[i + 1]) <= 47 or ord(s[i + 1]) >= 58) or i == len(s) - 1):
            num = int(num)
            if k <= num*len(x):
                X += x * int(num)
                num = "0"
                x = ""
                qans = X[k]
                X = ['#']
                return qans
            else:
                k -= (len(x) * num)
                num = "0"
                x = ""
                X = ['#']
        
    # Your code goes here
    return 































#taking inpit using fast I/O
def takeInput() :
    
    str1 = input().strip()
    k = int(input().strip())

    return str1, k

#main
str1, k = takeInput()
print(kThCharaterOfDecryptedString(str1, k))
