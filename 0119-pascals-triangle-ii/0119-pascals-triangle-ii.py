class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        ans = 1
        res.append(ans)
        for col in range(1,rowIndex+1):
            ans = ans * ((rowIndex+1) - col)
            ans = ans // col
            res.append(ans)
        return res    

        