# This code defines a 2D list (matrix) called
nums=[[5,6,7],[7,8,9],[1,2,3]]
rows = len(nums)
clo = len(nums[0])
print(rows)#3
print(clo)#3
for i in range(0,rows):
    for j in range(0,clo):
        print(nums[i][j],end=" ")
    print()#5 6 7
           #7 8 9
           #1 2 3
#------------------------------------------------------------
# This code prints the upper triangular   
nums=[[5,6,7],[7,8,9],[1,2,3]]
rows = len(nums)
clo = len(nums[0])
for i in range(0,rows):
    for j in range(0,clo):
        if j>=i:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
    
#------------------------------------------------------------
# This code prints the diagonal elements of the matrix
nums = [[5,6,7],[7,8,9],[1,2,3]]

rows = len(nums)
clo = len(nums[0])

for i in range(rows):
    for j in range(clo):
        if i == j:#00,11,22
            print(nums[i][j], end=" ")
    print()
    
#------------------------------------------------------------
# This code prints the anti-diagonal elements of the matrix
nums = [[5,6,7],[7,8,9],[1,2,3]]
n = len(nums)
for i in range(n):
    for j in range(n):
        if i + j == n - 1:#02,11,20:>862
            print(nums[i][j], end=" ")
    print()