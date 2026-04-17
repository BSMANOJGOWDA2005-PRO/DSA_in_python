#Find largest consecutive sequence in an array
nums =[1,99,101,98,2,3,5,100,1]
n = len(nums)
max_length = 0
for i in range(0,n):
    num = nums[i]#num=1,num=99,num=101,num=98,num=2,num=3,num=5,num=100,num=1
    count = 1
    while num + 1 in nums:#add 1+1 = 2 in the nums list checking
        count +=1
        num = num +1 #num=2,num=3,num=4(num+1) not in the list so loop will break
        max_length=max(max_length,count)
print(max_length)
#Tc=O(n^2) Because for and while loop
#Sc=O(1) because we are using constant space to store the count and max_length variables

#------------------------------------------------
nums=[1,99,101,98,2,5,3,100,1,1]
nums.sort()
smallest=float('-inf')
count = 0
largest = 0
n = len(nums)
for i in range(n):
    num = nums[i]
    if num-1==smallest:
        count +=1
        smallest=num
    elif num!=smallest:
        count =1
        smallest = num
    largest=max(largest,count)
    
print(largest)    
#Tc=O(nlogn) because of sorting the array
#Sc=O(1) 