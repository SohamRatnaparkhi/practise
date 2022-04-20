from bisect import bisect_left as bl,bisect_right as br
def bestInsertPos(arr, n, m):
    if len(arr) == 0:
        return 0
    # return bl(arr,m)
    return bin_search(arr, m, n)
def bin_search(l, x, m):
    s = 0
    e = m - 1

    while s <= e:
        mid = s + (e - s) // 2
        if l[mid] == x:
            return mid
        elif l[mid] > x:
            e = mid - 1
        else:
            s = mid + 1
    return e + 1

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = bestInsertPos(arr, n, m)
    print(f"Ans {_} = {ans}")