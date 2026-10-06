class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1

        while l < r:
            # Skip characters from the left
            # that are not letters or digits
            if not s[l].isalnum():
                l += 1

            # Skip characters from the right
            # that are not letters or digits
            elif not s[r].isalnum():
                r -= 1

            else:
                # Compare valid characters without case sensitivity
                if s[l].lower() != s[r].lower():
                    return False

                l += 1
                r -= 1

        return True