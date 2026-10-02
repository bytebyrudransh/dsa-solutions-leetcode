class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob, max_rob = 0, 0

        for current in nums:
            temp = max(max_rob, prev_rob + current)
            prev_rob, max_rob = max_rob, temp
        
        return max_rob