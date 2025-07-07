class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row , col = len(matrix),len(matrix[0])
        for i in range(col):
            maxi = float(-inf)
            for j in range(row):
                if matrix[j][i] > maxi:
                    maxi = matrix[j][i]
            for k in range(row):
                if matrix[k][i]==-1:
                    matrix[k][i]=maxi
        return matrix                    
