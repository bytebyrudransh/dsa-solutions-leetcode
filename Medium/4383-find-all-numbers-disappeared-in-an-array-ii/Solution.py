class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        arr = sorted(set(nums))
        N = len(arr)
        
        missing_integer_ranges = []

        index = bisect_left(arr, lower)
        start = end = lower
        for integer in range(lower, upper + 1):
            if index == N or integer != arr[index]:
                # missing integer
                end = integer
                continue
                
            if arr[index] != start:
                missing_integer_ranges.append([start, end])
            index += 1
            
            start = end = integer + 1
    
        if start <= upper:
            missing_integer_ranges.append([start, end])
        
        return missing_integer_ranges
