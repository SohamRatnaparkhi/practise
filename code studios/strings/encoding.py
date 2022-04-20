def encode(message):
    # Write your code here.
    ans = []
    i = 0
    while i < len(message):
        c = 0
        x = message[i]
        ans.append(x)
        while i < len(message) and message[i] == x:
            c += 1
            i += 1
        
        ans.append(str(c))
    return "".join(ans)

print(encode("aabbc"))
    