
input1 = "what up, daddy-o?"
input2 = "uh, not much"
input3 = "Yikes! my favorite racecar erupted!"
        # 01234567890123456789012345678901234
        # 00000000001111111111222222222233333

def longestPalindrome(myString):
    # variables
    newStr = ""
    paLst = []
    # code goes here

    for i in range(len(myString)):
        for j in range(len(myString)-1,i-1,-1):
            if i<j and myString[i] == myString[j]:
                l = j
                for k in range(i,j+1,1):
                    if myString[k] == myString[l]:
                        newStr = newStr + myString[k:k+1]
                        if k==j:
                            paLst.append(newStr)
                            newStr=""
                            break
                        else:
                            l=l-1
                    else:
                        newStr = ""
                        break
    if paLst == []:
        return print("This String contains no Palindrome")
    else:
        longestPal = max(paLst, key=len)
        if len(longestPal)<3:
            return print("This String contains no Palindrome")
        else:
            return print("The longest palindrome is - " +longestPal)


longestPalindrome(input3)


# input1 = "what up, daddy-o?"
# Output: "dad"

# Input: "uh, not much"
# Output: "u"

# Input: "Yikes! my favorite racecar erupted!"
# Output: "e racecar e"
