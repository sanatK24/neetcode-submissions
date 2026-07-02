class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        ## traverse the arr Prices; r doesnt go out of bounds
        while r < len(prices):
            ## profitability check
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] ## get profit
                maxP = max(maxP, profit) ## check max, current maxP or profit
            else:
                l = r
            r += 1
        return maxP