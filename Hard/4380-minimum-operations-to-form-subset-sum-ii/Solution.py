class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:

        n = len(nums)
        possible = []
        #we can use bfs to solve this problem
        def generate(num):
            q= deque([(num,0)])
            visited = set()
            visited.add(num)
            cost = {}

            while q :
                val,opt = q.popleft()

                if 0 < val <= sum:
                    cost[val] = opt

                # for nval in [val//2,val*2]:
                #     if nval > sum or nval < 0:
                #         continue
                        
                #     if nval not in visited:
                #         visited.add(nval)
                #         q.append((nval,opt+1))

                nval = val * 2

                if nval <= sum and nval not in visited:
                    visited.add(nval)
                    q.append((nval,opt+1))

                nval = val // 2

                if nval >0 and nval not in visited:
                    visited.add(nval)
                    q.append((nval,opt+1))

            return list(cost.items())

        possible=[generate(num) for num in nums]
        #print(possible)
        @cache
        def solve(i,rem):
            if rem == 0:
                return 0
            if i == n:
                return float('inf')




            ans=solve(i+1,rem)

            for v,c in possible[i]:
                if v <= rem:
                    
                    ans = min(ans,c+solve(i+1,rem - v))

            return ans

        res = solve(0,sum)

        if res == float('inf'):
            return -1

        return res
            

        
        
            

            
            