# Given an array of prices, find the maximum profit 
price = [7,2,1,5,6,4,8]
n = len(price)
maxi = 0
for i in range(0,n):
    for j in range(i+1,n):
        if price[j]>price[i]:#8>7otherswise we will get negative profit
            p=price[j]-price[i] #8-7=1
            maxi=max(maxi,p)#maxi=max(0,1)=1
print(maxi)#Finally we will get 7 as the maximum profit which is 8-1=7
#Tc=O(n^2) and Sc=O(1)

#-------------------------------------------------
#find the maximum profit in O(n) time complexity
price = [7,2,1,5,6,4,8]
min_prices=float("inf")#i=nfinity
maxi= 0
n=len(price)
for i in range(0,n):
    min_prices=min(min_prices,price[i])
    p = price[i]-min_prices
    maxi = max(maxi,p)
print(maxi)
#Tc=O(n) and Sc=O(1)

#-------------------------------------------------
#find the maximum profit in O(n) time complexity
#directly using min function to find the minimum price in the array
price = [7,2,1,5,6,4,8]
min_prices=float("inf")#i=nfinity
maxi= 0
n=len(price)
for i in range(0,n):
    min_prices=min(price)
    p = price[i]-min_prices
    maxi = max(maxi,p)
print(maxi)
#Tc=O(n) and Sc=O(1)