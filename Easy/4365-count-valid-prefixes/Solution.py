class Solution:
    def countValidPrefixes(self, s: str) -> int:

        ans = difference = 0

        for digit in s:
            if digit == '0':
                 difference+= 1
            else:
                difference-= 1

            if -2 < difference < 2:
                ans+= 1
                
        return ans