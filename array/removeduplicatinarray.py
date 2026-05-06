#By using set
num = [1, 2, 3, 4, 1, 5, 1, 2, 1, 2, 3]
print(set(num))


#By using list
num = [1, 2, 3, 4, 1, 5, 1, 2, 1, 2, 3]
result = []
for i in num:
    if i not in result:
        result.append(i)
print(result)


#By using dictionary
num = [1, 2, 3, 4, 1, 5, 1, 2, 1, 2, 3]
dic = {}
for i in num:
    dic[i]=0
print(dic)


#checking for duplicates
nums =[1,2,3,1]
found = False
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            found = True
            break
print(found)#output: True
         
    
   