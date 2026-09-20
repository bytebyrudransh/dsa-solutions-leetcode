class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if isinstance(flowerbed, list) and isinstance(n, int):

            total_count: int = 0
            spots_count: int = 1

            for spot in flowerbed:
                if spot == 0:
                    spots_count += 1
                else:

                    total_count += (spots_count - 1) // 2

                    spots_count = 0

                if total_count >= n:
                    return True

            if spots_count != 0:
                total_count += (spots_count // 2)
            return total_count >= n
        raise TypeError('Invalid input type')