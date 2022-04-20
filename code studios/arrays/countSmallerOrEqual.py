from bisect import bisect_left as bl,bisect_right as br
def countSmallerOrEqual(a, b, n, m):
    ans = []
    b.sort()
    # for x in a:
    #     a = br(b,x)
    #     ans.append(a)
    for x in a:
        f, g = bin_search(b, x, m)
        an = f if g is -2 else f + 1 
        ans.append(an)
    return ans

def bin_search(l, x, m):
    s = 0
    e = m - 1

    while s <= e:
        mid = s + (e - s) // 2
        if l[mid] == x:
            return mid, -1
        elif l[mid] > x:
            e = mid - 1
        else:
            s = mid + 1
    return s, -2




def main():
    for i in range(int(input())):
        n = int(input())
        a = list(map(int, input().strip().split()))
        m = int(input())
        b = list(map(int, input().strip().split()))
        x = countSmallerOrEqual(a, b, n, m)
        print(f"Ans {i + 1} - {x}")
    
main()