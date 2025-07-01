class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row in range(1,numRows+1):
            ans = 1
            temp = []
            temp.append(ans)
            for col in range(1,row):
                ans = ans * (row - col)
                ans = ans // col
                temp.append(ans)
            result.append(temp)
        return result        