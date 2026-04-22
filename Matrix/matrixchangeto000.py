def matrix_inf(matrix,row,col):
    rows = len(matrix)#4
    cols = len(matrix[0])#4
    
    for i in range(0,rows):
        if matrix[i][col] !=0:
            matrix[i][col]=float("inf")
    print(matrix)#[[7, 9, inf, 3], [10, 20, 0, 1], [29, 2, inf, 5], [4, 14, inf, 7]]...(0(m))
    
    for j in range(0,cols):
        if matrix[row][j]!=0:
            matrix[row][j]=float("inf")
    print(matrix)#[[7, 9, inf, 3], [inf, inf, 0, inf], [29, 2, inf, 5], [4, 14, inf, 7]]...(0(n))
    
    for i in range(0,rows):
        for j in range(0,cols):
            if matrix[i][j] == float("inf"):
                matrix[i][j]=0
    print(matrix)#[[7, 9, 0, 3], [0, 0, 0, 0], [29, 2, 0, 5], [4, 14, 0, 7]]....(0(m*n))
            
   
matrix = [[7,9,5,3],[10,20,0,1],[29,2,8,5],[4,14,6,7]]
matrix_inf(matrix,1,2)
#TC: O(m*n) where m is the number of rows and n is the number of columns in the matrix.......O(m) + O(n) + O(m × n)
#Sc: O(1) as we are modifying the matrix in place without using any additional data structures.