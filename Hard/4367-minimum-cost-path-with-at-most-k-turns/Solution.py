import heapq

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if m == 1 and n == 1:
            return grid[0][0]
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # dist[r][c][d][t]: min cost to reach (r, c) facing direction d with t turns
        dist = [[[[float('inf')] * (k + 1) for _ in range(4)] for _ in range(n)] for _ in range(m)]
        
        # (current_cost, r, c, direction, turns_used)
        pq = [(grid[0][0], 0, 0, -1, 0)]
        
        while pq:
            cost, r, c, d, t = heapq.heappop(pq)
            
            if r == m - 1 and c == n - 1:
                return cost
            
            if d != -1 and cost > dist[r][c][d][t]:
                continue
            
            for next_d, (dr, dc) in enumerate(dirs):
                nr = r + dr
                nc = c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    next_t = t + (1 if (d != -1 and d != next_d) else 0)
                    
                    if next_t <= k:
                        new_cost = cost + grid[nr][nc]
                        if new_cost < dist[nr][nc][next_d][next_t]:
                            dist[nr][nc][next_d][next_t] = new_cost
                            heapq.heappush(pq, (new_cost, nr, nc, next_d, next_t))
                            
        return -1