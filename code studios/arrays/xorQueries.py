def xorQuery(queries):
    # Write your code here.
    arr = []
    l = 0
    for q in queries:
        if q[0] == 1:
            arr.append(q[1])
            l += 1
        else:
            for x in range(l):
                arr[x] ^= q[1]
    return arr
		
    pass