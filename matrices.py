def get_col(matrix, col_n):
    if isinstance(matrix,list) and matrix != []:
        return get_col_aux(matrix,col_n, 0, 0,[])

def get_col_aux(matrix, col_n, i, j, col):
    if i == len(matrix):
        return col
    elif j == len(matrix[0]):
        return get_col_aux(matrix,col_n, i+1, 0, col)
    else:
        if col_n == j:
            val = matrix[i][j]
            col+= [val]
        return get_col_aux(matrix, col_n, i, j+1, col)

def mayorcol(matrix,col):
    if isinstance(matrix, list) and matrix != []:
        return mayorcol_aux(matrix, col, 1, matrix[0][col])

def mayorcol_aux(matrix,col,i,result):
    if i == len(matrix):
        return result
    else:
        if matrix[i][col] > result:
            result = matrix[i][col]
        return mayorcol_aux(matrix, col, i+1, result)

a = [[1,2,3,4],[5,16,7,8],[11,12,13,14]]
print (get_col(a,1))
print (mayorcol(a, 1))
