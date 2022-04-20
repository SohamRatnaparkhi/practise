def leftRotate(strr, d):    
    # Write your code here.
# 	ans = ""
	l = len(strr)
	d = d % l
	s = ""
	for i in range(d):
		s += strr[i]
	e = strr[d : l]
	return e + s
    
    
def rightRotate(strr, d):    
    # Write your code here.
	l = len(strr)
	d = d % l
	s = strr[0 : l - d]
	e = strr[l - d : l]
	return e + s
    

for i in range(int(input())):
    strr = input()
    d = int(input())
    ans = leftRotate(strr, d) + " " + rightRotate(strr, d)
    print(ans)
    print("------------------")
    