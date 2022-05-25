from sys import stdin, stdout, setrecursionlimit




def findTriplets(arr, n):
    # Write your code here
    ans = []
    arr.sort()
    for k in range(len(arr)):
        a = arr[k]
        i = 0 
        j = n - 1
        while ((i < n and j >= 0) and i < j) and (i != k and j != k):
            if arr[i] + arr[j] < -a:
                i += 1
            elif arr[i] + arr[j] > -a:
                j -= 1
            else:
                x = [a, arr[i], arr[j]]
                x.sort()
                if x not in ans:
                    ans.append(x)
                i += 1
                j -= 1

    # Return a list of triplets
    return ans
    pass





















# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    ans = findTriplets(arr, N)
    if len(ans) == 0:
        stdout.write("-1\n")
    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
