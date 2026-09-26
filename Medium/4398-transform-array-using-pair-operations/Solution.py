class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        sorelanuxi = (source, target)
        return sum(source) == sum(target)