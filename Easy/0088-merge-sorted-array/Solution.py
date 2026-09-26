class Solution:
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1        # Pointer for last element in nums1
        p2 = n - 1        # Pointer for last element in nums2
        i = m + n - 1     # Pointer for last position in nums1

        # Compare elements from the back
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1

            i -= 1

        # Copy remaining elements from nums2
        while p2 >= 0:
            nums1[i] = nums2[p2]
            p2 -= 1
            i -= 1