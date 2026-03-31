#find max of sub array
num = [-2,1,-3,4,-1,2,1,-5,4]
"""Let’s test some subarrays manually:
[4] = 4
[4,-1] = 3
[4,-1,2] = 5
[4,-1,2,1] = 6 ✅
[4,-1,2,1,-5] = 1
[4,-1,2,1,-5,4] = 5
"""
n=len(num)
maxi=float("-inf")
for i in range(0,n):
    total = 0
    for j in range(i,n):
        total+=num[j]
        maxi=max(maxi,total)
print(maxi)
 #TC -> O(n^2) - two loops
 #SC -> O(1) - constant space
#-----------------------------------------------------------------------------

#kadanes algorithm for subarry
num = [-2,1,-3,4,-1,2,1,-5,4]
n = len(num)
maxi = float("-inf")
total =0
for i in range(0,n):
    total = total+num[i]
    maxi = max(total,maxi)
    
    if total<0:
        total=0
print(maxi)
#TC -> O(n) - single loop
#SC -> O(1) - constant space



# [-2] -> total = -2, maxi = -2 -> reset total =0 -ve
# [1] -> total = 1, maxi = 1
# [1, -3] -> total = -2, maxi = 1 -> reset total = 0
# [4] -> total = 4, maxi = 4
# [4, -1] -> total = 3, maxi = 4
# [4, -1, 2] -> total = 5, maxi = 5
# [4, -1, 2, 1] -> total = 6, maxi = 6   # maximum
# [4, -1, 2, 1, -5] -> total = 1, maxi = 6
# [4, -1, 2, 1, -5, 4] -> total = 5, maxi = 6