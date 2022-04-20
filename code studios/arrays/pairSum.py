# def pairSum(arr, s):
#     # Write your code here.
#     arr = list((arr))
#     n = len(arr)
#     ans = []
#     arr.sort()
#     c = []
#     for i in range(len(arr)):
#         if BinarySearchAsc(arr, s - arr[i], 0, n - 1) != -1:
#             x = [arr[i], s - arr[i]]
#             # if x in ans:
#             #     continue
#             # else:
#             x.sort()
#             if c != x:
#                 ans.append(x)
#             c = x
#     # ans = list(set(ans))
#     # ans.sort()
#     return ans
def pairSum(arr, s):
    a=[]
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==s:
                #arr.remove(arr[i])
                a.append([arr[i], arr[j]])
    return a# Write your code here.
    pass
        
def BinarySearchAsc(l, target, s, e):
    """Searches a target element in array using binary search algorithm

    Args:
        l ([list]): [Array sorted in ascending order]
        target ([int]): [element to be searched]

    Returns:
        [integer]: [index of target element if it is found else - 1]
    """
    

    while(s <= e):
        mid = int(s + (e - s) / 2)
        
        if l[mid] > target:
            e = mid - 1
        elif l[mid] < target:
            s = mid + 1
        else:
            return l[mid]
    return -1

def main():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    x = pairSum(arr, s)
    print(x)


main()



def isValidPair(arr,n,k,m):
    
    # An odd length array cannot divided into pairs.
    if n%2 == 1:
        return False
    
    visited = [0] * n
    
    for i in range(n):
        for j in range(n):
            
            # If arr[i] and arr[j] is not included in any pair.
            if ( visited[i] == False and visited[j] == False):
                
                if ((arr[i] + arr[j])% k == m):
                    visited[i] = True
                    visited[j] = True
                    
                    '''
                        If any pair formed, then break and 
                        move to next pair that can be formed.
                    '''
                    break
                    
    # Check the condition if all the elements can be paired.
    for i in range(n):
        if visited[i] == False:
            return False
        
    return True