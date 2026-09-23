class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while True:
            middle_value = (left+right)//2
            result = guess(middle_value)

            if result > 0:
                left = middle_value + 1
            elif result < 0:
                right = middle_value - 1
            else:
                return middle_value
                