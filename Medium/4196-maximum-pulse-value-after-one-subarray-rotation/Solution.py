# Try 1 time O(n) space O(1)
class Solution:
    def maxValue(self, nums: list[int]) -> int:
        n = len(nums)
#pulse value 
        S = 0
        prev_odd = float('inf')
        prev_even = float('inf')
        min_even = float('inf')

        for i in range(n):
            val = nums[i] if i % 2 == 0 else -nums[i]
            S += val

            if i == 0:
                prev_odd = val
            else:
                curr_odd = min(val, prev_even + val)
                curr_even = prev_odd + val
                min_even = min(min_even, curr_even)

                prev_odd = curr_odd
                prev_even = curr_even

        max_delta = 0
        if min_even < 0:
            max_delta = -2 * min_even

        return S + max_delta