#graph using matrix method
'''
1 ----- 2
|       |
|       |
3 ----- 4
 \     /
   \ /
    5
'''
n = 5
m=6
edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[4,5]]

matrix=[[0] *(n+1) for _ in range(n+1)]#list comperhension method 
#[0,0,0,0,0,0] for_in range(5+1):
#[[0, 0, 0, 0, 0, 0]...........up t0 6 times [0, 0, 0, 0, 0, 0]]
print(matrix)

for u,v in edges:
    matrix[u][v]=1 #m[1][2]=1 ....1=row and 2=col [0, 0, 1, 0, 0, 0]
    matrix[v][u]=1#m[2][1] 2=row and 1= col [0, 1, 0, 0, 0, 0]
    
print(matrix)#[[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], 
#[0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0]]
    