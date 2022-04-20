from sys import stdin, stdout
import numpy as np

def printArrayAfterKOperations(arr, N, K):
	a = np.array(arr)
	mx = a.max()
	mx2 = 0
   # Write your code here.
	for i in range(K):
# 		for i in range(N):
# 			z = mx - arr[i]
# 			if z > mx2:
# 				mx2 = z
# 			arr[i] = z
		a = a - mx
		mx = a.max()
	return a.tolist()
   # Return a list representing the updated array.
   


























# Taking input using fast I/0.
def takeInput():
    N, K = list(map(int, stdin.readline().strip().split(" ")))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, K, arr


tc = int(input())
while tc > 0:
    N, K, arr = takeInput()
    sol = printArrayAfterKOperations(arr, N, K)
    for i in sol:
        stdout.write(str(i) + " ")
    stdout.write("\n")
    tc -= 1
