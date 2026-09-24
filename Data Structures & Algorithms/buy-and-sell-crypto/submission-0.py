class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for p in prices:
            if p < lowest_price:
                lowest_price = p
            if (profit := p - lowest_price) > max_profit:
                max_profit = profit

        return max_profit

