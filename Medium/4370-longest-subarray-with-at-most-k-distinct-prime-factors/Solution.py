class Solution:

    def longestSubarray(self, nums: list[int], k: int) -> int:

        def primeFactors(x):

            factors = set()

            d = 2

            while d * d <= x:

                if x % d == 0:

                    factors.add(d)

                    while x % d == 0:
                        x //= d

                d += 1

            if x > 1:
                factors.add(x)

            return factors


        left = 0
        right = 0
        n = len(nums)

        maxi = 0
        freq = {}

        while right < n:

            # Add right element
            temp = primeFactors(nums[right])

            for num in temp:

                if num not in freq:
                    freq[num] = 1
                else:
                    freq[num] += 1


            # Shrink window if invalid
            while len(freq) > k:

                temp = primeFactors(nums[left])

                for num in temp:

                    freq[num] -= 1

                    if freq[num] == 0:
                        del freq[num]

                left += 1


            # Current window is valid
            maxi = max(maxi, right - left + 1)

            right += 1


        return maxi