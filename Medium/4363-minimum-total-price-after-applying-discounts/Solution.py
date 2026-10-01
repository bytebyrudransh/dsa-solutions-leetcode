class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        
        result = 0.0
        
        for i in range(len(prices)):
            if i < len(discounts):
                result += prices[i] * (100 - discounts[i]) / 100.0
            else:
                result += prices[i]
                
        return result