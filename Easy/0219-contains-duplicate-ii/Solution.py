class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary={}
        for index,value in enumerate(nums):
            if value in dictionary and index-dictionary[value]<=k:
                return True
            dictionary[value]=index
        return False