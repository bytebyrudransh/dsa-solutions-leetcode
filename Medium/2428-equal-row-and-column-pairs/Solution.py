class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        my_dict = Counter([tuple(grid[i]) for i in range(n)])
 
        s = 0
        for i in range(len(grid)):
            col = [grid[j][i] for j in range(len(grid))]
            if tuple(col) in my_dict:
                s += my_dict[tuple(col)]
        return s