class Solution:
    def rotateMatrix(self, mat):
        # Reverse each row
        for row in mat:
            row.reverse()
        # Reverse the order of rows
        mat.reverse()
        return mat
