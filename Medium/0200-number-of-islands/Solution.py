class Solution:
    def dfs(self, r, c, nums, track, count):
        if r<0 or r >= len(nums) or c<0 or c >= len(nums[0]):
            return
        if nums[r][c] == "0": 
            return 
        if track[r][c] != 0 and nums[r][c] == "1":
            return
        track[r][c] = count
        self.dfs(r+1, c, nums, track, count)
        self.dfs(r-1, c, nums, track, count)
        self.dfs(r, c+1, nums, track, count)
        self.dfs(r, c-1, nums, track, count)

    def numIslands(self, nums: List[List[str]]) -> int:
        m, n = len(nums), len(nums[0])
        track = [[0]*n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if nums[i][j] == "1" and track[i][j] == 0:
                    count += 1
                    self.dfs(i, j, nums, track, count) 
        ans = 0
        for i in range(m):
            for j in range(n) :
                if track[i][j] >= ans:
                    ans = track[i][j]
        return ans