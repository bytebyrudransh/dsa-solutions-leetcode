class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        before_prev = nums[0]
        curr = prev = max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(nums[i] + before_prev , prev)
            before_prev = prev
            prev = curr    
        return curr