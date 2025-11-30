class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        n=len(mat)
        m=len(mat[0])
        
        first_row_zero=False
        first_col_zero=False
        
        for j in range(m):
            if mat[0][j]==0:
                first_row_zero=True
        for i in range(n):
            if mat[i][0]==0:
                first_col_zero=True
        for i in range(1,n):
            for j in range(1,m):
                if mat[i][j]==0:
                    mat[i][0]=0
                    mat[0][j]=0
        for i in range(1,n):
            for j in range(1,m):
                if mat[i][0]==0 or mat[0][j]==0:
                    mat[i][j]=0
        if first_row_zero:
            for j in range(m):
                mat[0][j]=0
        if first_col_zero:
            for i in range(n):
                mat[i][0]=0
                    