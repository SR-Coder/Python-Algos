#! Joey Gaston / Jim Reeder/BradSittner
# Zip

# Given two lists of equal length as input, "zip" the lists into a dictionary.

# Input: ['a', 'b', 'c'], [1, 2, 3]
# Output: {
# 'a': 1,
# 'b': 2,
# 'c': 3
# }


# codewars.com


def zip(lst1, lst2):

    dictionaryOfWords = {}
    for i in range(len(lst1)):
        dictionaryOfWords[f"{lst1[i]}"] = lst2[i]
    return dictionaryOfWords


list_1 = ['a', 'b', 'c']
list_2 = [1, 2, 3]

print(zip(list_1, list_2))


# Invert Dictionary

# Create a function to swap dictionary keys to values, and values to keys.

# for pair in pairs
# pair.key = temp
# pair.key = pair.value
# pair.vlaue = temp

def invertDict(myDict):
    newDict = {}
    for key in myDict:
        print(key)
        print(myDict[key])
        newDict[myDict[key]] = key
    return newDict


input_1 = {"name": "Zaphod", "charm": "high", "morals": "dicey"}

print(invertDict(input_1))


# Output: {Zaphod: "name", high: "charm", dicey: "morals"}


# create fucntion
# create input dictionary
# create undefined dictionary w/ {a : 0, b : 0, c : 0 }
# for loop to iterate through "input dic"
# it replace current key: values of undefined dictionairy w/ inverted key:values from input dictionary
