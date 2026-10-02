class Solution:
    def maxValue(self, nums: List[int]) -> int:
        nums[1::2] = (-num for num in nums[1::2])
        half_delta = 0
        for arr in nums, nums[1:]:
            curr_sum = 0
            for pair in batched(arr, 2):
                pair = tuple(pair)
                if len(pair) == 2:
                    pair_sum = sum(pair)
                    curr_sum = min(curr_sum + pair_sum, pair_sum)
                    half_delta = min(half_delta, curr_sum)
        return sum(nums) - 2*half_delta