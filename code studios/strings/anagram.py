from collections import defaultdict
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def def_value():
    return 0

def getMinimumAnagramDifference(str1, str2):
    # Write your code here.
    str1 = list(str1)
    str2 = list(str2)
    if len(str1) != len(str2):
        return -1
    else:
        str1.sort()
        str2.sort()
        f1 = defaultdict(def_value)
        f2 = defaultdict(def_value)
        ans = 0
        for i in range(len(str1)):
            
            f1[str1[i]] += 1
            f2[str2[i]] += 1
        # print(f1)
        # print(f2)
        # if len(f1.keys()) <= len(f2.keys()):
                
        for key in f1.keys():
            x = f1[key]
            # if f2[key] != 0:
            y = f2[key]
            ans += (abs(f1[key] - f2[key]))
            f2[key] = 0
            f1[key] = 0
     
        for key in f2.keys():
            
            y = f2[key]
            # if f1[key != 0]:
            x = f1[key]
            ans += (abs(f1[key] - f2[key]))

        return ans//2
    
    

# Taking Input.
def takeInput():
    str1 = stdin.readline().strip()
    str2 = stdin.readline().strip()
    return str1, str2

# Main.
T = int(stdin.readline().strip())
for i in range(T):
    str1, str2 = takeInput()
    ans = getMinimumAnagramDifference(str1, str2)
    print(ans)