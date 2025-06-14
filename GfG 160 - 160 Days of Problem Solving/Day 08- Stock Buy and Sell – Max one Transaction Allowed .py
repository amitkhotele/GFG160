class Solution:
    def maximumProfit(self, prices):
        buyPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] > buyPrice:
                maxProfit = max(maxProfit, prices[i] - buyPrice)
            else:
                buyPrice = prices[i]

        return maxProfit
