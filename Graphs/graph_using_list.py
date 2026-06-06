#list using matrix method
'''
1 ----- 2
|       |
|       |
3 ----- 4
 \     /
   \ /
    5
'''

n=5
e=6
edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[4,5]]

lit = [[] for i in range(n+1)]#[[], [], [], [], [], []]
print(lit)

for u,v in edges:
    lit[u].append(v)#list[1].append(2) output:[2, 3]
    lit[v].append(u)#list[2].append(1) output:[1, 4]
print(lit)
'''[
    [],
    [2, 3], 
    [1, 4], 
    [4, 1, 5],
    [2, 3, 5],
    [3, 4]
    ]
'''