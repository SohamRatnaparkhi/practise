from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

def findTriplets(arr, n, z):
    ans = []
    arr.sort()
    for k in range(len(arr)):
        a = arr[k]
        i = 0 
        j = n - 1
        while ((i < n and j >= 0) and i < j) and (i != k and j != k):
            if arr[i] + arr[j] + a < z:
                i += 1
            elif arr[i] + arr[j] + a > z:
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

















# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    K = int(stdin.readline())
    return N, arr,K


tc = int(input())
while tc > 0:
    N, arr,K = takeInput()
    ans = findTriplets(arr, N,K)

    if len(ans) == 0:
        stdout.write("-1\n")

    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
