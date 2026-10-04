class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 + nums2
        a.sort()
        length = len(a)
        if length % 2 == 0:
            return (a[length//2]+a[length//2 -1]) /2
        else:
            return a[length//2]