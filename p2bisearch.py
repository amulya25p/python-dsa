# rotated sorted list given 
# rotated n no of times
# target no is given which lies inside the rotated list
# find the position of the target no in the rotated sorted list

def position(list, num):
    lo=0
    hi=len(list)-1
    while True:
       mid=(lo+hi)//2
       if list[mid]==num:
        return mid
       elif list[mid]>list[hi]:
        if list[mid]>num:
            lo=mid+1
        else:
            hi=mid-1
       else:
        if list[mid]<num:
            lo=mid+1
        else:
            hi=mid-1
    return -1
        

list=[5,6,9,0,2,3,4]
num=2
print(list," ", num)
nr=position(list,num)
print("positio== ", nr)