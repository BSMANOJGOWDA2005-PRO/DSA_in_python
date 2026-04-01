#Rearrange the array in such a way that positive and negative numbers are placed alternatively.
num=[5,10,-3,-1,-10,6]
positive = [5,10,6]
negative = [-3,-1,-10]
n=len(positive)
for i in range(0,n):
    num[2*i]=positive[i]#num[0]=5,num[2]=10,num[4]=6
    num[(2*i)+1]=negative[i]#num[1]=-3,num[3]=-1,num[5]=-10
print(num)#Finally we will get the output as [5, -3, 10, -1, 6, -10]
#Tc=O(n) for traversing the array once
#Sc=O(n) because we are using extra space to store the positive and negative numbers separately

#--------------------------------------------------
#Rearrange the array in such a way that positive and negative numbers are placed alternatively.
num=[5,10,-3,-1,-10,6]
n=len(num)
result=[0]*n
positive,negative=0,1#positive=0,negative=1 
for i in range(0,n):
    if num[i]>=0:#
        result[positive]=num[i]#result[0]=5,result[2]=10,result[4]=6
        positive +=2 #incrementing the positive index by 2 to place nexy=t ele in result
    else:
        result[negative]=num[i]#result[1]=-3,result[3]=-1,result[5]=-10
        negative+=2
print(result)#Finally we will get the output as [5, -3, 10, -1, 6, -10]
#Tc=O(n) for traversing the array once 
#Sc=O(n) because we are using an extra array to store the resultS