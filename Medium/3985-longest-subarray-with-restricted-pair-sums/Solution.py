class Solution:
    def maxSubarray(self, nums: list[int]) -> int:
        l, ans = 0, 0
        
        # Maps a pair sum to the maximum index 'k' of the elements that formed it.
        # Default value is -1 to indicate the sum hasn't been formed yet.
        two_sum = defaultdict(lambda: -1)
        
        # Maps a number to its most recent index in the array.
        # Default value is -1 to indicate the number hasn't been seen yet.
        used_num = defaultdict(lambda: -1)
        
        for r, num in enumerate(nums):
            # Condition 1: If the current number 'num' is already a sum of two elements 
            # within the current valid window [l...r-1], we must shrink the window.
            if two_sum[num] >= l:
                l = two_sum[num] + 1
                
            # Check all possible pairs formed by the current 'num' and previous elements in the window.
            for k in range(l, r):
                s = nums[k] + num
                
                # Condition 2: If the new pair sum 's' matches a single number that already 
                # exists inside the current window, it forms an invalid triplet.
                # We must shrink the left pointer past either the existing number or 'k'.
                if used_num[s] >= l:
                    l = min(used_num[s], k) + 1
                
                # Update the latest index 'k' where this pair sum 's' was generated.
                if k > two_sum[s]:
                    two_sum[s] = k
                    
            # Record the current number's position
            used_num[num] = r
            
            # Calculate the maximum length of a valid subarray found so far
            ans = max(r - l + 1, ans)
            
        return ans