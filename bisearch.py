# list in decreasing order
# find given no, traversing the list in
# as few times as possible.

#liner search approach
# def position(list, num):
#     p=0
#     while True:
#         if(list[p]==num):
#             return p
#         p+=1
#         if p==len(list):
#             return -1      

# list=[3,6,7,5,9]
# num=0
# spc=position(list,num)
# print(list)
# print(num)
# print('the no found at',spc)

#binary search for reducing time complexity


from http.client import FOUND
from turtle import left, right

def condition(mid):
        if list[mid]==num:
            return FOUND
        if list[mid]<num:
            return right
        if list[mid]>num:
            return left 

def bipos(list, num):
    lo=0
    hi=len(list)-1
    while lo<=hi:
        mid=(lo+hi)//2
        result=condition(mid)
        if result==FOUND:
            return mid
        if result==left:
            hi=mid-1
        if result==right:
            lo=mid+1
    return -1

list=[4,6,7,8,9,20]
print(list)
num=20
print(num)
r=bipos(list,num)
print('result= ', r)