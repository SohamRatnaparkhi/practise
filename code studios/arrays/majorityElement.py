from collections import defaultdict
def def_value():
    return 0
def majorityElementII(arr):
	freq = defaultdict(def_value)
	n = len(arr) // 3
	for i in arr:
        
		freq[i] += 1
	ans = []
	for x in freq.keys():
		if freq[x] > n:
			ans.append(x)
	return ans

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = majorityElementII(arr)
    print(f"Ans {_} = {ans}")
    pass
