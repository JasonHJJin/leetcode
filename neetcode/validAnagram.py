def isAnagram(self, s: str, t: str) -> bool:

    output = sorted(s)

    output2 = sorted(t)

    if output != output2:
        return False
    else:
        return True




print(isAnagram("", "rat", "car"))