class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0;
        b = 0
        s = 1
        while b < len(prices) and s < len(prices):
            if prices[b] >= prices[s]:
                b = s
                s += 1
            else:
                profit = max(profit,prices[s]-prices[b])
                s += 1
        return profit
        