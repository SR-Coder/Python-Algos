# Remove Duplicates

# Given a SORTED list of integers, dedupe the list 

# Because list elements are already in order, all duplicate values will be grouped together.
# Ok to use a new list
def removedup(listy_list):
    new_list=[]
    for i in listy_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
listy_list=[1,1,2,3,3,3]

print(removedup(listy_list))
# Bonus: do it in O(n) time (no nested loops, new list ok)
# Bonus: Do it in-place (no new list)

def removeDupInPlace(myList):
    # read in a list
    # find Duplicates
    # delete Duplicates
    for i in range(len(myList)):
        if i<len(myList)-1:
            if myList[i]== myList[i+1]:
                myList.pop(i)
            if i>0:
                if myList[i] == myList[i-1]:
                    myList.pop(i)

    return myList

listy_list=[1,1,1,1,1,2,2,2,2,3,3,4,4,4,4,4,4,5,5] 
print(removeDupInPlace(listy_list))

# Bonus: Do it in-place in O(n) time and no new list
# Challenge: Keep it O(n) time even if it is not sorted

listy_list=[1,1,1,1,1,2,2,2,2,3,3,4,4,4,4,4,4,5,5] 
listy_list = list(set(listy_list))
print(listy_list)