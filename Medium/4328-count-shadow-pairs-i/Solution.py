class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        n = len(nums)
        stack = []
        cnt = Counter()
        ret = 0
        for v in nums:
            while stack and stack[-1] > v:
                cnt[stack.pop()] -= 1
            ret += len(stack) - cnt[v]
            stack.append(v)
            cnt[v] += 1
        return ret
            
            