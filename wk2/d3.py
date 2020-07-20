
# String: Dedupe
# Remove duplicate characters - (case-sensitive)

# Input: "abcABC"
# Output: "abcABC"

# Input: "helloo"
# Output: "helo"


def dedupe(myString):
    aNewStr = ""
    for char in myString:
        if char not in aNewStr:
            aNewStr = aNewStr + char
    return aNewStr




def dedupe2(myString):
    newStr = "".join(set(myString))
    return newStr








# Given a string containing space separated words
# Reverse each word in the string.

# Input: "hello"
# Output: "olleh"

# Input: "hello world"
# Output: "olleh dlrow"

sentence = 'hello world'

def reverseStatement(sentence):
    newSent = ""
    newlist =[]
    newlist = sentence.split(" ")
    for i in newlist:
        newSent = newSent+ " "
        for ch in i[::-1]:
        newSent = newSent + ch
    print(newSent)

    return newSent

print(reverseStatement(sentence))