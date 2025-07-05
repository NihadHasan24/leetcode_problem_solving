class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = {}
        for i in range(len(arr)):
            if arr[i] not in res:
                res[arr[i]] = 1
            else:
                res[arr[i]] += 1
        maxi = -1
        for i,j in res.items():
            if i == j:
                maxi = max(maxi,i)
        return maxi    
