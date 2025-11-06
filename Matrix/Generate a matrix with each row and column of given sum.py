class Solution:
    def generateMatrix(self, rowSum, colSum):
        n = len(rowSum)
        m = len(colSum)
        mat = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                # Assign the minimum possible value to cell
                val = min(rowSum[i], colSum[j])
                mat[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val

        return mat
