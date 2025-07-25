class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #Transpose matrix
        for i in range(n-1):
            for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i],matrix[i][j]    
        #Reversing each row 
        for i in range(n):
            matrix[i].reverse()  
        return matrix           