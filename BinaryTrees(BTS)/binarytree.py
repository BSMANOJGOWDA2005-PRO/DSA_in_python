class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.rigth=None
        
drinks=Node("drinks")
hot =Node("hot")
cold =Node("cold")
tea =Node("tea")
coffee =Node("coffee")
cola =Node("cola")
fanta =Node("fanta")

drinks.left=hot
drinks.rigth=cold
hot.left=tea
hot.rigth=coffee
cold.left=cola
cold.rigth=fanta


print(drinks.left.val)#hot
print(drinks.rigth.val)#cold
print(hot.left.val)#tea
print(hot.rigth.val)#coffee
print(cold.left.val)#cola
print(cold.rigth.val)#fanta
