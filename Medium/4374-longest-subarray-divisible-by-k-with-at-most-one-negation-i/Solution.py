class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for left in range(n):
            total = 0
            residues = set()

            for right in range(left, n):
                total += nums[right]
                residues.add(nums[right] % k)

                # Case 1: Subarray sum is already divisible by k
                if total % k == 0:
                    ans = max(ans, right - left + 1)
                    continue

                s = total % k

                # Case 2: Negate one element
                # New sum = total - 2*x
                # We need:
                # total - 2*x ≡ 0 (mod k)
                # Therefore:
                # 2*x ≡ total (mod k)

                if k % 2 == 1:
                    # k is odd, so 2 has an inverse modulo k
                    inv2 = (k + 1) // 2
                    needed = (s * inv2) % k

                    if needed in residues:
                        ans = max(ans, right - left + 1)

                else:
                    # k is even
                    # 2*x ≡ s (mod k) is possible only when s is even
                    if s % 2 == 0:
                        needed = (s // 2) % (k // 2)

                        for r in residues:
                            if r % (k // 2) == needed:
                                ans = max(ans, right - left + 1)
                                break

        return ans