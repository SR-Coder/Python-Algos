x = "Live from New York, it's Saturday Night!"
y = "there's no free lunch - gotta pay yer way."

def firstLetter(someString):
    splitString = someString.split()
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    # print(splitString)
    new_string = ""
    for i in range(len(splitString)):
        temp = splitString[int(i)]
        temp = temp[:1]
        temp = temp.capitalize()
        if temp in letters:
            new_string = new_string + temp
        # print(new_string)
    return(new_string)

print(firstLetter(y))



# String: Reverse
# create a function 
# split the letters into an list
# revers order of list
# concat letters into string
z = "creature"
def reverse_string(str):
    # myList=[]
    # for i in range(len(str)+1):
    #     temp = str[i-1:i]
    #     myList.append(temp)
    # for i in range(len(myList),1,-1):
    #     newStr = newStr + myList[i]
    # return newStr
    # 
    temp = str[::-1]
    # print(temp)
    return temp
    
print(reverse_string(z))
# Examples
# Input: "creature"
# Output: "erutaerc"