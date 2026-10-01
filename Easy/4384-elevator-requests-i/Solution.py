class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total_time = 0
        current_floor = 0
        
        for floor in requests:
            total_time += abs(floor - current_floor)
            current_floor = floor
            
        return total_time