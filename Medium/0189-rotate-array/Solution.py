class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k == 0:
            return
        
        count = 0
        start = 0

        while count < n:
            current_idx = start
            item_in_hand = nums[start]
            
            while True:
                next_idx = (current_idx + k) % n
                nums[next_idx], item_in_hand = item_in_hand, nums[next_idx]
                current_idx = next_idx
                count += 1

                if current_idx == start:
                    break
            
            start += 1