# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: 
# the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will 
# represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string 
# containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.

# For example: if strArr contains ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] the output should return "1,4,13" because 
# those numbers appear in both strings. The array given will not be empty, and each string inside the array will 
# be of numbers sorted in ascending order and may contain negative numbers.


def FindIntersection(strArr):
    a = strArr[0]
    b = strArr[1]
    temp = []
    a = a.split(',')
    b = b.split(',')
    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(b)):
        b[i] = int(b[i])

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] and a[i] != ",":
                temp.append(a[i])
    if len(temp) == 0:
        return False
    else:
        for i in range(len(temp)):
            for j in range(len(temp)):
                if temp[i] < temp[j]:
                    tmp = temp[j]
                    temp[j] = temp[i]
                    temp[i] = tmp
        temp = [str(element) for element in temp]
        strArr = ",".join(temp)

    return strArr


# keep this function call here
print(FindIntersection(["1,3,4,7,13", "1,2,4,13,15"]))
