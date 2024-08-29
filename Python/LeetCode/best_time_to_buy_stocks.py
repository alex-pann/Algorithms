class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = [[]]
        n = len(prices)

        for i in range(0, n-1):
            for j in range(i+1, n):
                profits[i].append(prices[j] - prices[i])

        return profits


prices = [7,1,5,3,6,4]

# s = Solution()
# profit = s.maxProfit(prices)

profits = []
n = len(prices)

for i in range(0, n-1):
    profits.append([])
    for j in range(i+1, n):
        profits[i].append(prices[j] - prices[i])

print(profits)