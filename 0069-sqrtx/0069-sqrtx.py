class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                low = mid + 1
            else:
                high = mid - 1  
        return high       
        # if x == 0 or x == 1:
        #     return x
        # ans = 0
        # for i in range(x):
        #     if i * i <= x: 
        #         ans = i
        #     else:
        #         break
        # return ans        

