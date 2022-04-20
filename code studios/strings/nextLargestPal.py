from math import log
from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)


def nextLargestPalindrome(str1, length):
    sl = list(map(int, str1))
    a = list(map(int, str1))
    allnine = False
    allsame = False
    for i in range(length - 1):
        if a[i] == a[i + 1]:
            allsame = True
            if a[i] == 9:
                allnine = True
            else:
                allten = False
        else:
            allsame = False
        
    if allnine:
        return str(int(str1) + 2)
    elif allsame:
        if length & 1 == 1:
            if a[length // 2 != 9]:
                a[length // 2] = a[length // 2] + 1
            else:
                mx = max(a[length // 2 - 1], a[length // 2 + 1])
                a[length // 2 - 1] = mx
                a[length // 2 + 1] = mx
            return "".join(map(str, a))
        else:
            a[length // 2] = a[length // 2] + 1
            a[length // 2 - 1] = a[length // 2 - 1] + 1
            return "".join(map(str, a))
    else:
        s = length // 2 - 1
        e = length // 2
        if length & 1 == 1:
            e += 1
        while s >= 0 and e < length:
            mx = max(a[s], a[e])
            a[s] = mx
            a[e] = mx
            s -= 1
            e += 1
        if a == sl:
            if length & 1 == 1:
                if a[length // 2 != 9]:
                    a[length // 2] = a[length // 2] + 1
                else:
                    mx = max(a[length // 2 - 1], a[length // 2 + 1])
                    a[length // 2 - 1] = mx
                    a[length // 2 + 1] = mx
                return "".join(map(str, a))
            else:
                a[length // 2] = a[length // 2] + 1
                a[length // 2 - 1] = a[length // 2 - 1] + 1 
        return "".join(map(str, a))

        
        
	
   





























# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    S = stdin.readline().strip()
    return N, S


tc = int(input())
i = 0
while tc > 0:
    
    N, S = takeInput()
    S = nextLargestPalindrome(S, N)
    stdout.write(f"ans {i} " + S + "\n")
    i  += 1
    tc -= 1
