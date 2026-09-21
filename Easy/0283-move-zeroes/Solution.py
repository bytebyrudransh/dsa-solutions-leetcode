class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        for i in nums:
            if i==0:
                nums.pop(nums.index(i))
                nums.append(0)