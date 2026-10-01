class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_representation = self._build_binary_string(s)
        return self._is_palindrome(binary_representation)

    def _build_binary_string(self, s: str) -> str:
        """Convert each character to its 8-bit ASCII binary code and concatenate."""
        char_binaries = [self._to_8bit_binary(ord(char)) for char in s]
        return "".join(char_binaries)

    def _to_8bit_binary(self, ascii_value: int) -> str:
        """Convert an integer to an 8-bit binary string, zero-padded on the left."""
        bits = []

        while ascii_value > 0:
            ascii_value, remainder = divmod(ascii_value, 2)
            bits.append(str(remainder))

        while len(bits) < 8:
            bits.append("0")

        return "".join(reversed(bits))

    def _is_palindrome(self, text: str) -> bool:
        """Check if a string reads the same forwards and backwards."""
        left, right = 0, len(text) - 1

        while left < right:
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1

        return True