class Solution:
    def countSpecialIntegers(self, nums):
        mp = {}

        n = len(nums)

        mp[nums[0]] = 1

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                mp[nums[i]] = mp.get(nums[i], 0) + 1

        cnt = 0

        for value in mp.values():
            if value == 1:
                cnt += 1

        return cnt