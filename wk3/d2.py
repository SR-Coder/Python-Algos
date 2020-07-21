# Binary Search


def binarySearch(srtdList, num):
    start = 0
    end =  len(srtdList)-1
    mid = (start + end)//2
    while 1 != 2:
        print(start, end, mid, "these are positions")
        print(srtdList[start], srtdList[end], srtdList[mid], "these are values")
        if num == srtdList[mid]:
            print('success', num, srtdList[mid])
            return True
        if num > srtdList[mid]:
            start = mid
            mid = (start+end)//2
        if num < srtdList[mid]:
            end = mid
            mid = (start+end)//2
            
        
    

listy = [1,2,3,4,5,6,7,8,9]
num = 3

print(binarySearch(listy, num))