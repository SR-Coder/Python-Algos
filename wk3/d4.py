# Given an int to represent how much change is needed
# calculate the fewest number of coins needed to create that change,
# using the standard US denominations


# Input: 25
# Output: { "quarter": 1 }

# Input: 50
# Output: { "quarter": 2 }

# Input: 9
# Output: { "nickel": 1, "penny": 4 }

# Input: 99
# Output: { "quarter": 3, "dime": 2, "penny": 4 }

def howMuchChange(myChange):
    print(myChange)
    first = myChange/25
    quarter, change = divmod(first,1)
    change = round(change,2) * 25
    change = change / 10
    dimes, change = divmod(change,1)
    change = round(change,2) * 10
    change = change / 5
    nickle, change = divmod(change,1)
    change = round(change,2) * 5
    pennies = change 
    print("quarters:", quarter,'dimes: ', dimes, 'nickles: ',nickle, 'pennies: ',pennies)

    listOfChange = {}
    if quarter != 0:
      listOfChange = {"quarters":int(quarter)}
    if dimes != 0:
      listOfChange.update({"dimes": int(dimes)})
    if nickle != 0:
      listOfChange.update({"nickles": int(nickle)})
    if pennies != 0:
      listOfChange.update({"pennise":int(pennies)})
    
    return listOfChange

print(howMuchChange(137))