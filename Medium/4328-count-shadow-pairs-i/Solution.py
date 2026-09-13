#try 1 try 2 
from collections import defaultdict
from bisect import bisect_right

class Solution(object):
    def shadowPairs(self, nums):
        n = len(nums)
        
        R = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                R[stack.pop()] = i
            stack.append(i)
            
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
            
        ans = 0
        for i in range(n):
            length = R[i] - i - 1
            if length > 0:
                val = nums[i]
                left_idx = bisect_right(pos[val], i)
                right_idx = bisect_right(pos[val], R[i] - 1)
                equal_count = right_idx - left_idx
                ans += length - equal_count
                
        return ans

    def __getattr__(self, name):
        return self.shadowPairs
                

        
    