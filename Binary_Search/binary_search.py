# Binary Search Algorithm Implementation
def binary_search(nums):
    n=len(nums)
    low = 0
    high=n-1
    target =11
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target :
            low = mid+1
        else:
            high= mid-1
    return -1
                     
nums=[2,4,6,7,9,11,18,19]
r=binary_search(nums)
print(r)#output:5
#Tc->Time Complexity: O(log n)
#Sc->Space Complexity: O(1)

#-----------------------------
#Recursion approach
def binary_search(nums,low,high):
    if low>high:
        return -1
    target = 19
    mid = (low+high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid]<target:
        return binary_search(nums,mid+1,high)
    else:
        return binary_search(nums,low,mid-1)
nums=[2,4,6,7,9,11,18,19]
result=binary_search(nums,0,len(nums)-1)
print(result)
#Tc->Time Complexity: O(log n)
#Sc->Space Complexity: O(log n)
    
    