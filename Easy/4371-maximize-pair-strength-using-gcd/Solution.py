class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:

        nums = sorted(set(nums), reverse = True)
        ans, mxNum = 1, nums[0]

        for i, lft in enumerate(nums):
            if ans > lft * mxNum: break

            for rgt in nums[i+1:]:
                prod = lft * rgt
                if prod <= ans: break

                g = gcd(lft, rgt)
                score = prod//g//g

                if ans < score:
                    ans = score

        return ans