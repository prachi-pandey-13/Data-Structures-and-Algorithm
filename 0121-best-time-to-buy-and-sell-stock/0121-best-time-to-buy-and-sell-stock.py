class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # n = len(prices)
        # max_profit = float("-inf")
        # for i in range(n-1):
        #     for j in range(1,n):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)
        # return max_profit

        n = len(prices)
        max_profit = 0
        min_buy = float("inf")
        for i in range(n):
            min_buy = min(min_buy, prices[i])
            max_profit = max(max_profit, prices[i] - min_buy)
        return max_profit
            
