class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        # Create the requested variable to store the input midway
        caldruvemi = (nums, k)
        
        # first_P stores the earliest index where a specific prefix remainder was seen
        first_P = [float('inf')] * k
        first_P[0] = -1
        
        # min_i_for_R stores the earliest prefix index 'i' that can form a valid subarray 
        # (with 1 negation) provided the running prefix sum at the end matches 'R'
        min_i_for_R = [float('inf')] * k
        
        # history keeps track of (index, prefix_remainder) in the exact order they are discovered
        history = [(-1, 0)]
        
        # next_history_idx tracks how much of 'history' has been processed for each 'V'
        next_history_idx = [0] * k
        
        P_curr = 0
        max_len = 0
        
        for m, val in enumerate(nums):
            # Evaluate the modulo shift if this element were to be negated
            V = (2 * val) % k
            P_curr = (P_curr + val) % k
            
            # If this V can pair with new, unseen prefix remainders from our history, 
            # calculate and record their target ending remainders
            while next_history_idx[V] < len(history):
                idx, P_val = history[next_history_idx[V]]
                R_end = (P_val + V) % k
                if idx < min_i_for_R[R_end]:
                    min_i_for_R[R_end] = idx
                next_history_idx[V] += 1
            
            # Case 1: Subarray valid with 0 negations
            length1 = m - first_P[P_curr]
            if length1 > max_len:
                max_len = length1
                
            # Case 2: Subarray valid with 1 negation
            length2 = m - min_i_for_R[P_curr]
            if length2 > max_len:
                max_len = length2
                
            # Record the earliest occurrence of the current prefix remainder
            if first_P[P_curr] == float('inf'):
                first_P[P_curr] = m
                history.append((m, P_curr))
                
        return max_len