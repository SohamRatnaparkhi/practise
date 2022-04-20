def matchSpecificPattern(n, words, pattern):
    # Write your code here
    # Return a list of words
    ans = []
    for word in words:
        l = len(word)
        if l != len(pattern):
            continue
        if l == 1:
            ans.append(word)
            continue
        cnt = 0
        for i in range(l):
            for  j in range(i + 1, l - 1):
                if abs(ord(word[i]) - ord(word[j])) == abs(ord(pattern[i]) - ord(pattern[j])):
                    # ans.append(word)
                    cnt += 1
        if cnt == (l-1) * (l-2) // 2:
            ans.append(word)
    return ans
for i in range(int(input())):
    print(matchSpecificPattern(input(), (input()).split(), input()))