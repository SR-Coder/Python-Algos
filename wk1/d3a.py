# Jim Reeder /
# String: Is Palindrome

# Create a function that returns a boolean whether the string is a strict palindrome.
# - palindrome = string that is same forwards and backwards

# Do not ignore spaces, punctuation and capitalization

# 1 need to loop through a string forwards
#   increment of 1
# 2 loop through a string backwards
#    through the whole string
# 3 check for same letters or spaces
# 4 move one step to left or right respectively and check
#    check for same letters and spaces
# test1 = "a x a"
# test2 = "Dud"
# def isPalindrome(myString):
#     for i in range(len(myString)):
#         j = len(myString)-1-i
#         if myString[i] != myString[j]:
#             return False
#         else:
#             return True


# print( isPalindrome(test1))


# Input: "a x a"
# Output: true

# Input: "racecar"
# Output: true

# Input: "Dud"
# Output: false


# Longest Palindrome

# For this challenge, we will look not only at the entire string provided, but also at the substrings within it.
# Return the longest palindromic substring.

# Strings longer or shorter than complete words are OK.
# All the substrings of "abc" are:
# a, ab, abc, b, bc, c

# 1 need to loop through a string forwards
#   increment of 1
# 2 loop through a string backwards
#    through the whole string
# 2a aka find a palendrome and save its length
# 3 check for same letters or spaces
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
        # print("next test" )
        for j in range(len(myString)-1,i-1,-1):
            # print(i,j)
            if i<j and myString[i] == myString[j]:

                l = j
                for k in range(i,j+1,1):
                    
                    if myString[k] == myString[l]:
                        # print("success")
                        newStr = newStr + myString[k:k+1]
                        # print(myString[k],myString[l],k,l,i,j)
                        # print(newStr)
                        if k==j:
                            # print("create new item in paList")
                            paLst.append(newStr)
                            newStr=""
                            # print(paLst)
                            break
                        else:
                            l=l-1
                    else:
                        newStr = ""
                        #print("sorry not a palendrome") #debuging line
                        break
    if paLst == []:
        return "This String contains no Palindrome"
    else:
        longestPal = max(paLst, key=len)
        if len(longestPal)<3:
            return "This String contains no Palindrome"
        else:
            return "The longest palindrome is - " +longestPal


print(longestPalindrome(input3))


# input1 = "what up, daddy-o?"
# Output: "dad"

# Input: "uh, not much"
# Output: "u"

# Input: "Yikes! my favorite racecar erupted!"
# Output: "e racecar e"
