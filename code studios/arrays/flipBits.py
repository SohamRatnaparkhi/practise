from cv2 import FarnebackOpticalFlow
from matplotlib.colors import rgb2hex


arr = [1, 0, 1, 0, 1, 0, 1, 0]
n = 8
def flipBits(arr, n): 
    # Write your code here
    ans = 0
    one = 0
    for i in range(n):
        z,o = 0,0
        if arr[i] == 1:
            one += 1
        for j in range(i, n):
            if arr[j] == 0:
                z += 1
            else:
                o += 1

        
            ans = max(ans, z - o)
    print(ans + one)

    pass

flipBits(arr, n)

def flipBits(arr, n): 
    mxv = 0
    ones = 0
    
    # Consider all SubArrays by using two nested two loops
    for i in range(n):
        if (arr[i] == 1): 
            ones += 1
            
        c1 = 0
        c0 = 0
        for j in range(i, n):
            if (arr[j] == 1): 
                c1 += 1
            else:
                c0 += 1
            mxv = max(mxv, c0 - c1)
    result = ones + mxv
    return result