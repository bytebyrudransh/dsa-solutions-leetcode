class Solution:
    def trap(self, height: list[int]) -> int:
        # first la irundu middle varen
        left = 0

        # last la irundu middle varen
        right = len(height) - 1

        # left side la iruka periya block size
        left_max_wall = 0

        # right side la iruka periya block size
        right_max_wall = 0

        # total ah evlo water store aaguthu
        stored_water = 0

        # rendu pointers meet pandra varikum loop odum
        while left < right:

            # left block chinnatha irundha left side process pannuvom
            if height[left] <= height[right]:

                # current block maximum wall vida perusa irundha
                # maximum wall ah update pannuvom
                if height[left] > left_max_wall:
                    left_max_wall = height[left]

                # current block maximum wall vida chinnatha irundha
                # anga water store aagum
                else:
                    stored_water += left_max_wall - height[left]

                # left pointer next block ku move aagum
                left += 1

            else:

                # right block chinnatha irundha right side process pannuvom
                if height[right] >= right_max_wall:
                    right_max_wall = height[right]

                # current block maximum wall vida chinnatha irundha
                # anga water store aagum
                else:
                    stored_water += right_max_wall - height[right]

                # right pointer previous block ku move aagum
                right -= 1

        return stored_water