
from sys import stdin

def getProductArrayExceptSelf(arr, n):
    x = 1
    zero = 0
    i = -1
    for y in range(n):
        if arr[y] == 0:
            zero += 1
            i = y
            continue
        x *= arr[y]
	# if zero == False:
    #     for y in range(n):
    #         arr[y] = x // arr[y]
    #     return arr
    if zero == 0:
        for y in range(n):
            arr[y] = x // arr[y]
        return arr    
    elif zero == 1:
        for y in range(n):
            if arr[y] != 0:
                arr[y] = 0
            else:
                arr[y] = x
        return arr
    else:
        return [0] * n

        
	








































def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n

def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ") 
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    product = getProductArrayExceptSelf(arr, n)
    printList(product, n)
    
    t -= 1