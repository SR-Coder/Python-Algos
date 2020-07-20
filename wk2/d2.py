# Jim Reeder / nathan ostby / Joseph Ramos
# Given a list of strings
# return a sum to represent how many times each list item is found (a frequency table)

input1 = ['a', 'a', 'a']
# Output: {
#     a: 3
#   }

input2 = ['a', 'b', 'a', 'c', 'B', 'c', 'c', 'd']
# Output: {
#     a: 2,
#     b: 1,
#     c: 3,
#     B: 1,
#     d: 1
#   }
# pass in an input wihch is a list (we will have to iterate through a list)
# setup a for loop to look at each item in list
# check to see if it matches anything
# create a blank dictionary
#  if item in list is in dictionary than add 1 to its value
#  if item is not in list add key as item and value as 1
# then create a dictionary with the results


def counter(myList):
    letterCount = {}
    for i in myList:
        if i in letterCount:
            letterCount[f'{i}'] = int(letterCount[f'{i}'])+1
        else:
            letterCount[f'{i}'] = 1
    print(letterCount)
    pass


counter(input1)







# Reverse Word Order
# Create a function that, given a string of words (with spaces), returns a new string with words in reverse sequence.

input3 = "This is a test"
# Output: "test a is This"

# create a function that accepts a string
# pass a string to the function
# figure out what the last word is
# copy last word to new string
# add a space
# repeat until no more words
# print final string

def reverse(myString):
    newString = ""
    temp = len(myString)
    for i in range(len(myString)-1,-1,-1):
        if myString[i].isspace() == True or i==0:
            for j in range(i,temp,1):
                if j == temp-1:
                    print('end')
                    newString = newString + myString[j]
                    temp = i+1
                else:
                    print('new')
                    newString = newString + myString[j]
            print(newString)
            
            
    
    return newString

print(reverse(input3))