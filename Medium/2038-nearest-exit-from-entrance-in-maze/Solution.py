
from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Directions for moving in 4 possible ways (down, right, up, left)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        rows, cols = len(maze), len(maze[0])
        x0, y0 = entrance
        
        # Use a queue for BFS with (row, col, steps)
        queue = deque([(x0, y0, 0)])
        maze[x0][y0] = '+'  # Mark entrance as visited to prevent re-visiting

        while queue:
            x, y, steps = queue.popleft()

            # Explore all four directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == '.':
                    # If we reach an exit that is not the entrance
                    if new_x in [0, rows - 1] or new_y in [0, cols - 1]:
                        return steps + 1  
                    
                    # Mark cell as visited and add to queue
                    maze[new_x][new_y] = '+'
                    queue.append((new_x, new_y, steps + 1))

        return -1  # No exit found