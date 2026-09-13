# I just wasted time here 
from bisect import bisect_left, bisect_right

class Solution(object):
    def shadowPairs(self, nums):
        INF = float('inf')
        
        def dnc(left, right):
            if left >= right: 
                return 0
            
            mid = (left + right) // 2
            ans = dnc(left, mid) + dnc(mid + 1, right)

            L_vals = nums[left:mid+1]
            U_L = sorted(list(set(L_vals)))
            K_L = len(U_L)
            bit_min = [INF] * (K_L + 1)
            
            min_g = [INF] * (mid - left + 1)
            for i in range(mid, left - 1, -1):
                V = nums[i]
                rev_start = K_L - bisect_right(U_L, V)
                res = INF
                idx = rev_start
                while idx > 0:
                    if bit_min[idx] < res: 
                        res = bit_min[idx]
                    idx -= idx & (-idx)
                min_g[i - left] = res
                
                rank = bisect_left(U_L, V) + 1
                rev_rank = K_L - rank + 1
                idx = rev_rank
                while idx <= K_L:
                    if V < bit_min[idx]: 
                        bit_min[idx] = V
                    idx += idx & (-idx)

            R_vals = nums[mid+1:right+1]
            U_R = sorted(list(set(R_vals)))
            K_R = len(U_R)
            bit_max = [-INF] * (K_R + 1)
            
            max_l = [-INF] * (right - mid)
            for j in range(mid + 1, right + 1):
                V = nums[j]
                rank_q = bisect_left(U_R, V)
                res = -INF
                idx = rank_q
                while idx > 0:
                    if bit_max[idx] > res: 
                        res = bit_max[idx]
                    idx -= idx & (-idx)
                max_l[j - (mid + 1)] = res
                
                rank = bisect_left(U_R, V) + 1
                idx = rank
                while idx <= K_R:
                    if V > bit_max[idx]: 
                        bit_max[idx] = V
                    idx += idx & (-idx)

            P = []
            U_X_set = set()
            for i in range(mid - left + 1):
                P.append((nums[left + i], min_g[i]))
                U_X_set.add(nums[left + i])
                
            Q = []
            for j in range(right - mid):
                Q.append((nums[mid + 1 + j], max_l[j], nums[mid + 1 + j] - 1))
                
            P.sort(key=lambda x: x[1], reverse=True)
            Q.sort(key=lambda x: x[0], reverse=True)
            
            U_X = sorted(list(U_X_set))
            M = len(U_X)
            bit_sum = [0] * (M + 1)
            
            p_idx = 0
            for q in Q:
                y_query, x_low, x_high = q
                while p_idx < len(P) and P[p_idx][1] >= y_query:
                    px = P[p_idx][0]
                    rank = bisect_left(U_X, px) + 1
                    idx = rank
                    while idx <= M:
                        bit_sum[idx] += 1
                        idx += idx & (-idx)
                    p_idx += 1
                    
                rank_high = bisect_right(U_X, x_high)
                rank_low = bisect_left(U_X, x_low) + 1
                
                if rank_high >= rank_low:
                    s_high = 0
                    idx = rank_high
                    while idx > 0:
                        s_high += bit_sum[idx]
                        idx -= idx & (-idx)
                        
                    s_low = 0
                    idx = rank_low - 1
                    while idx > 0:
                        s_low += bit_sum[idx]
                        idx -= idx & (-idx)
                        
                    ans += (s_high - s_low)
                    
            return ans

        return dnc(0, len(nums) - 1)