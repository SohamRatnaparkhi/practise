def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    # flag1 = False
    # flag2 = False
    # z = 0
    # diff = -1
    # for i in range(n - 1):
    #     x = arr[i]
        
    #     if not flag1:
    #         y = arr[i + 1]
    #         diff = abs(x - y)
    #     if diff == 1:
    #         flag1 = True
    #         z = y
    #     if flag1:
    #         diff = abs(z - x)
    #         if diff == 1:
    #             flag2 = True
    # return flag1 & flag2
    pass

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = lengthOfLongestConsecutiveSequence(arr, n)
    print(f"Ans {i} = {ans}")
    pass
