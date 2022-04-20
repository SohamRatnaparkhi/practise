def getLengthofLongestSubstring(s, k):

    # Write your code here.
	l = len(s)
	m = 0
	for i in range(l):
		for j in range(l):
			x = s[i : j + 1]
			y = len(x)
			l1 = len(list(set(list(x))))
			if l1 <= k:
				if y > m:
					m = y
	return m
    
for i in range(int(input())):
    
    k = int(input())
    s = input()
    ans = getLengthofLongestSubstring(s, k)
    print(ans)
    print("------------------")
    