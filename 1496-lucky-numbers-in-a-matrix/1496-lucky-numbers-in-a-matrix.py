class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row , col = len(matrix) , len(matrix[0])
        for r in range(row):
            mini = float(inf)
            inx = 0
            for c in range(col):
                if matrix[r][c] < mini:
                    mini = matrix[r][c]
                    inx = c
            maxi = float(-inf)        
            for k in range(row):
                if matrix[k][inx] > maxi:
                    maxi = matrix[k][inx] 
            if mini == maxi:
                return [maxi]
        return []        

                   
                     

        