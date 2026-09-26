class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        # Traverse all elements through loop...
        for i in nums:

            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k      