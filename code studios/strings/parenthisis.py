def minimumParentheses(pattern):

    # Write your code here
	p = 0
	q = 0
	for l in pattern:
		if l == '(':
			p += 1
		elif l == ')':
			q += 1
	return abs(p - q)
    # Return the minimum number of parentheses required.
    
for _ in range(int(input())):
    print(minimumParentheses(input()))