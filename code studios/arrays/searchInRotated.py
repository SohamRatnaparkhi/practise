peak = 0
def search(arr, target) :
    # Write your code here.
    n = len(arr)
    peak = findPeak(arr, n)
    if n == 1:
        if arr[0] == target:
            return 0
        else:
            return -1
    if arr[peak] == target:
        return peak
    s,e = 0,peak - 1
    left = False
    while s <= e:
        mid = s + (e - s) // 2
        if arr[mid] == target:
            left = True
            return mid
        elif arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    right = False
    if left == False:
        s = peak 
        e = n - 1
        while s <= e:
            mid = s + (e - s) // 2
            if arr[mid] == target:
                right = True
                return mid
            elif arr[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
    if left == False and right == False:
        return -1
    pass

def findPeak(arr, n):
    s = 0
    e = n - 1

    while s <= e:
        mid = s + (e - s) // 2
        if ((mid  < e) and (arr[mid] > arr[mid + 1])):
            return mid
        elif ((mid  > s) and arr[mid] < arr[mid - 1]):
            return mid - 1
        elif arr[mid] > arr[s]:
            s = mid + 1

        elif arr[mid] <= arr[s]:
            
            e = mid - 1

    return -1

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    p = findPeak(arr, n)
    global peak 
    peak = p
    for _ in range(int(input())):
        q = int(input())
        # 
        x = search(arr, q)
        print(f"Ans for {q} = {x}")
        
        
main()