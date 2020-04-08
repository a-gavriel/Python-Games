def mayor_col(matrix, col_n):
    if isinstance(matrix,list) and matrix != []:
        return get_col(matrix,col_n, i, j,col )

def get_col(matrix, col_n, i, j, col):
    if i == len(matrix):
        print (matrix)
        return matrix
    elif j == len(matrix[0]):
        return get_col(matrix,col_n, i+1, 0, col)
    else:
        if col_n == col:
            col+=[matrix[i][j]]
        return get_col(matrix, col_n, i, j+1, col)


a = [[1,2,3,4],[5,6,7,8],[11,12,13,14]]
mayor_col(a,2)
