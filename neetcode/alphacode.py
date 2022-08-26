d = {} #empty dictionary
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    d[alpha[i]] = i #assigns the key value as alphabets and corresponding index value from alpha string as the value for the key


def alphacode(s):

    count = 0

    if s == '0':
        return 1

    for i in range(len(s)):

        if s[i] in d:
            count += 1
            s = s[1:]
    
    for j in range(len(s)):

        if int(s[:j+2]) >= 27 and int(s[:j+2]) < 10:
            j += 1
            continue
        else:
            count += 1
            s = s[1:]

    return count + 1
        

print(alphacode(input()))


