class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        maximum_profit = 0

        for i in range(1, len(prices)):
            current_profit = prices[i] - minimum_price

            if current_profit > maximum_profit:
                maximum_profit = current_profit

            if prices[i] < minimum_price:
                minimum_price = prices[i]

        return maximum_profit