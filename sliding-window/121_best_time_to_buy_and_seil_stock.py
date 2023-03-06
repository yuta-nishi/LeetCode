# n=len(prices)
# Time: O(n)
# Space: O(1)


class Solution:
    def maxProfit(self, prices: list) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            cur_profit = prices[right] - prices[left]
            if cur_profit > 0:
                max_profit = max(max_profit, cur_profit)
            else:
                left = right
            right += 1
        return max_profit


# Time: O(n)
# Space: O(1)


class Solution:
    def maxProfit(self, prices: list) -> int:
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
