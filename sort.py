#bubble, insertion, merge, quick

from tkinter.messagebox import NO


def bubblesort(nums):
    for i in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1]=nums[i+1], nums[i]
    return nums

def insertionsort(nums):
    #The pop(postion) method removes the element at the specified position. 
    #The insert(position, element) method inserts the specified value
    #at the specified position. 
    for i in range(len(nums)):
        cur=nums.pop(i)
        j=i-1
        while j>=0 and nums[j]>cur:
            j-=1
        nums.insert(j+1,cur)
    return nums

def merge(nums1, nums2):
    merged=[]
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<=nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1
    nums1_remain=nums1[i:]
    nums2_remain=nums2[j:]
    return merged + nums1_remain + nums2_remain


def mergesort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    lnums=nums[:mid]
    rnums=nums[mid:]

    left_sort, right_sort=mergesort(lnums), mergesort(rnums)
    sortnums=merge(left_sort,right_sort)
    return sortnums

def partition(nums, lo=0, hi=None):
    if hi is None:
        hi=len(nums)-1
    l,r=lo,hi-1
    while r>l:
        if nums[l]<=nums[hi]:
            l+=1
        elif nums[r]>nums[hi]:
            r-=1
        else:
            nums[l],nums[r]=nums[r],nums[l]
    if nums[l]>nums[hi]:
        nums[l],nums[hi]=nums[hi],nums[l]
        return l
    else:
        return hi

def quicksort(nums,lo=0,hi=None):
    if hi is None:
        nums=list(nums)
        hi=len(nums)-1
    while lo<hi:
        pivot=partition(nums, lo, hi)
        quicksort(nums, lo, pivot-1)
        quicksort(nums,pivot+1,hi)
    return nums


mylist=[5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
print(mylist)
print(quicksort(mylist))

