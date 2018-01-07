def checkPalindrome(inputString):
    print inputString
    print inputString[::-1]
    if inputString==inputString[::-1]:
        return True
    else:
        return False
print checkPalindrome('abac')
print checkPalindrome('aba')
print checkPalindrome('abaccaba')
print checkPalindrome('aaaa')
print checkPalindrome('baba')
