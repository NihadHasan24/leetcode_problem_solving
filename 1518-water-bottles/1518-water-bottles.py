class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles 
        while numBottles >= numExchange:
            Exchange = numBottles // numExchange
            ans += Exchange
            remain = numBottles % numExchange
            numBottles = Exchange + remain
        return ans
        