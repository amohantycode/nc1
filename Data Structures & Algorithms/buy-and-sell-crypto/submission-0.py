class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        g = 0
        for v in prices:
            if v < minP:
                minP = v
            potentialP = v-minP
            g = max(potentialP, g)
        return g
