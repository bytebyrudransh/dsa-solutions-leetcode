class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        result = []
        maxVal = max(candies)

        for c in candies:
            result.append(c + extraCandies >= maxVal)

        return result