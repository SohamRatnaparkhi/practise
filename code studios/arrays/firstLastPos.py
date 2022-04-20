from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def findFirstLastPosition(arr, n, x):
    # Write your code here.
    
    ans = [BinarySearchAsc(arr, x, 0, n - 1, True), BinarySearchAsc(arr, x, 0, n - 1, False)]
    # Return a tuple containing two integers denoting the first and last occurrence of X.
    return ans
    pass

def BinarySearchAsc(l, target, s, e, left):
    """Searches a target element in array using binary search algorithm

    Args:
        l ([list]): [Array sorted in ascending order]
        target ([int]): [element to be searched]

    Returns:
        [integer]: [index of target element if it is found else - 1]
    """
    
    ans = -1
    while(s <= e):
        mid = int(s + (e - s) / 2)
        
        if l[mid] > target:
            e = mid - 1
        elif l[mid] < target:
            s = mid + 1
        else:
            ans = mid
            if left:
                e = mid - 1
            elif not left:
                s = mid + 1

    return ans














# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    X = int(stdin.readline())
    return N, arr, X


tc = int(input())
while tc > 0:
    N, arr, X = takeInput()
    ans = findFirstLastPosition(arr, N, X)
    stdout.write(str(ans[0]) + " " + str(ans[1]) + "\n")
    tc -= 1
