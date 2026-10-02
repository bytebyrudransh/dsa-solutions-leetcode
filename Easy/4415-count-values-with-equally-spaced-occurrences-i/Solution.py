class Solution:
    def countSpecialIntegers(self, nums):
        freq = [0] * 101

        for x in nums:
            freq[x] += 1

        res = 0

        for x in range(1, 101):
            if freq[x] == 3:
                first = -1
                second = -1
                third = -1

                for i, num in enumerate(nums):
                    if num == x:
                        if first == -1:
                            first = i
                        elif second == -1:
                            second = i
                        else:
                            third = i
                            break

                if second - first == third - second:
                    res += 1

        return res