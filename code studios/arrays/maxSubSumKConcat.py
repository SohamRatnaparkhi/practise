def maxSubSumKConcat(arr, n, k):
    i = 0
    j = 0
    sm, mx = 0,0
    
    while i < n*k:
        if i % n == 0:
            j = 0
        sm += arr[j]
        mx =  max(mx, sm)
        if sm < 0:
            sm = 0
        j += 1
        i += 1
        
    return mx

for i in range(int(input())):
    n, k = map(int,input().strip().split())
    arr = list(map(int, input().split()))
    print("__________")
    print(maxSubSumKConcat(arr, n, k))