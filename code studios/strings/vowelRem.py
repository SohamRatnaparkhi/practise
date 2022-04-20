def removeVowels(inputString):
    # Write your code here.
# 	inputString = list(inputString)
	vowels = ['a','e','i','o','u','A','E','I','O','U']
	ans = ''
	for l in inputString:
		if l not in vowels:
			ans += l
	return ans


