class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)

        took = prices[0] + prices[1]

        if money - took>=0:
            return money - took
        else:
            return money