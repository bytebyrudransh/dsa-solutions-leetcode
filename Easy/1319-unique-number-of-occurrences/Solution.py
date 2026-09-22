class Solution(object):
    def uniqueOccurrences(self, arr):
        hashMap = {}

        for num in arr:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        hashSet = set()
        flag = True
        
        for count in hashMap.values():
            if count in hashSet:
                flag = False
                break
            else:
                hashSet.add(count)
        
        return flag

        