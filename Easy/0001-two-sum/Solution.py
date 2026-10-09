class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_set = set(nums) # O(n)

        for i in range(len(nums) - 1): # O(n)
            y = target - nums[i]

            if y in nums_set: # O(1)
                for j in range(i + 1, len(nums)): # O(n)
                    if i != j and nums[j] == y:
                        return [i, j]
