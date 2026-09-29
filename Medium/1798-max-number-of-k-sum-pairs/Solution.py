class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        hash_map = {}
        hash_map[nums[0]] = 1
        count = 0
        for i in range(1,len(nums)):
            diff = k - nums[i]
            
            # find the diff in the hash_map if found decrease the freq
            if diff in hash_map and hash_map[diff]>0:
                hash_map[diff] -= 1
                    
                if nums[i] in hash_map and hash_map[nums[i]]>0:
                    hash_map[nums[i]] -= 1
                count += 1
                continue
            
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] += 1

        return count

            
            
            