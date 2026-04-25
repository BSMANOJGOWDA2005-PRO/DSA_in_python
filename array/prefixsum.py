#prefix sum
def p(nums,left,rigth):
    n = len(nums)
    total = 0
    for i in range(left,rigth+1):
        if left <=rigth:
            total = total+nums[i]
           
    return total
nums=[-2,0,3,-5,-1]
re =p(nums,0,2)
print(re)
            