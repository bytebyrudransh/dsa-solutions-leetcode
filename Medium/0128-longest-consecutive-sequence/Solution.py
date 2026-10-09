class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        set_nums = set(nums)
        longest = 0

        for num in nums:

            if num in set_nums and num - 1 not in set_nums:

                length = 1
                next_num = num + 1

                set_nums.remove(num)

                while next_num in set_nums:
                    length += 1
                    set_nums.remove(next_num)
                    next_num += 1

                longest = max(longest, length)

        return longest