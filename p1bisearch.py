# list of numbers, obtained by rotating a sorted list an 
# unknown number of times.
# find the minimum no of times the original sorted list was rotated
# to obtain the given list. 
# You can assume that all the numbers in the list are unique.

def rotate(list):
    lo=0
    hi=len(list)-1
    while True:
        mid=(lo+hi)//2
        if list[mid]<list[mid-1]:
            return mid
        elif list[mid]<list[hi]:
            hi=mid-1
        else:
            lo=mid+1
    return -1

list=[3,5,7,8,9,10]
print(list)
nr=rotate(list)
print('the no of rotations== ', nr)
        