test1 = "(()))"
test2 = " (((()))) "


# def validParens(myString):
#     res = []
#     for i in myString:
#         if i == "(":
#             res.append(i)
#         if i == ")":
#             if len(res)>0:
#                 res.pop()
#             else:
#                 return False
#     if len(res)==0:
#         return True
#     else:
#         return False


# print(validParens(test1))


def validBrackets(myString):
    res = []
    bLeft = ['(','{','[']
    bRight = [')','}',']']
    for char in myString:
        if char in bLeft:
            res.append(char)
        if char in bRight:
            if char ==')':
                if res[-1] == '(':
                    res.pop()
    print(res)
    return res

validBrackets(test2)