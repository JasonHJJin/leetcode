def isValid(self, s: str) -> bool:

    if len(s) <= 1:
        return False

    dict = { '(' : ')', '{' : '}', '[' : ']'}

    s = s + "0"

    lis = list(map(str, s))

    print(lis)
    print(len(lis))


    for i in range(len(lis)):

        print(i)

        if lis[i+1] == "0":
            break
        
        elif (dict[lis[i]] == lis[i+1]):
            i+=1
            continue
            
        else:
            return False

    return True


print(isValid("", "()[]"))