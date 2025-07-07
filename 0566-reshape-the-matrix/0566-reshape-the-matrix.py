class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row , col = len(mat),len(mat[0])
        if row * col != r * c:
            return mat
        res = [[] for _ in range(r)]
        i = j = 0
        for r in range(r):
            for _ in range(c):
                res[r].append(mat[i][j])
                j += 1
                if j >= col:
                    j = 0
                    i += 1
        return res            

