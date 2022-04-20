from collections import defaultdict as dd
def val():
    return 0
def findNonRepeating(s):
    freq = dd(val)
    print(freq)
    for i in s:
        freq[i] += 1
    for key in freq.keys():
        if freq[key] == 1:
            return key
    return "#"
    pass
# print(findNonRepeating(input()))
for i in range(int(input())):
    print(findNonRepeating(input()))