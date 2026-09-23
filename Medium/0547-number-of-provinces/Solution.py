from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        n_provinces = 0

        visited = [0] * n

        def bfs(start):
            q = deque()
            q.append(start)
            visited[start] = 1

            while q:
                city = q.popleft()

                # Check every possible city connected to current city
                for neighbor in range(n):

                    if isConnected[city][neighbor] == 1 and visited[neighbor] == 0:
                        visited[neighbor] = 1
                        q.append(neighbor)

        for city in range(n):

            if visited[city] == 0:
                bfs(city)
                n_provinces += 1

        return n_provinces
