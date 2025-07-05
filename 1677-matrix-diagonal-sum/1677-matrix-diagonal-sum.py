class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        for i in range(n):
            total += mat[i][i]
        for i in range(n):
            j = n - 1 - i
            if j != i:
               total += mat[i][j]
        return total            
        