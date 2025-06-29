class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        ans = 0
        for i in range(x):
            if i * i <= x: 
                ans = i
            else:
                break
        return ans        

