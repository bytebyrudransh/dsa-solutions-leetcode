class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        # Every operation preserves the total sum.
        # If both totals are equal, we can fix each position
        # one by one and leave the remaining difference in one index.
        return sum(source) == sum(target)