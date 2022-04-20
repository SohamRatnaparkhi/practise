from sys import stdin

def possibleToMakeTriangle(arr):

    # Write your function here.
    arr.sort()
    for i in range(len(arr) - 2):
        if arr[i] + arr[i + 1] > arr[i + 2]:
            return True
    return False

# Main code.
t = int(input().strip())

for i in range(t):
    n = list(map(int, stdin.readline().strip().split(" ")))

    if len(n) > 1:
        arr = n
    else:
        arr = list(map(int, stdin.readline().strip().split(" ")))

    if (possibleToMakeTriangle(arr)):
        print("YES")
    else:
        print("NO")
