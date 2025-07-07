class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        row , col = len(grid),len(grid[0])
        for i in range(row):
            if grid[i][i]!=0:
                grid[i][i]=0
            else:
                return False    
        for j in range(row):
            if j == (row-1-j):
                pass
            elif grid[j][row-1-j]!=0:
                  grid[j][row-1-j]=0
            else:
                return False      
        for i in range(row):
            for j in range(col):
                if grid[i][j]!=0:
                    return False

        return True