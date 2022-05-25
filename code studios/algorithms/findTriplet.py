from sys import stdin, stdout, setrecursionlimit
answers = []
def findTriplet(arr, n):
    # Write your code here
    arr.sort()
    for k in range(len(arr)):
        a = arr[k]
        i = 0 
        j = n - 1
        while ((i < n and j >= 0) and i < j):
            if i == k:
                i += 1
            if j == k:
                j -= 1
            if arr[i] + arr[j] < a:
                i += 1
            elif arr[i] + arr[j] > a:
                j -= 1
            else:
                return [a, arr[i], arr[j]]
                i += 1
                j -= 1

    # Return a list of triplets
    return []

def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    ans = findTriplet(arr, N)
    if len(ans) == 0:
        answers.append("false")
    else:
        answers.append("true")
        
    tc -= 1
check = ["false"
,"true"
,"true"
,"true"
,"true"
,"false"
,"true"
,"true"
,"false"
,"false"
,"true"
,"true"
,"true"
,"true"
,"false"]
print("------------------")
for i in range(len(answers)):
    if answers[i] != check[i]:
        print(i)
