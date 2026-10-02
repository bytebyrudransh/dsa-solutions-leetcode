
class Solution:
    def guessNumber(self, n: int) -> int:
        high = n
        low = 1

        while low < high:
            mid = (high + low) // 2
            val = guess(mid)

            if val == 0:
                return mid
            elif val == -1:
                high = mid - 1
            else:
                low = mid + 1
        return low


        