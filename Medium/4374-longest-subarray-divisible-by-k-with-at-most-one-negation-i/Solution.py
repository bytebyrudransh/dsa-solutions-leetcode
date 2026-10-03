class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        # i am pretty sure my idea is correct just something 
        # if i changed it at the  j then the value remains same for [j+1 to i] only changes at 
        # print((2-(1)+(-1%6))%6)
        n=len(nums)
        prefix=[0]*(n)
        mp=defaultdict(list)
        prefix[0]=(nums[0])%k
        nums[0]%=k
        for i in range(1,n):
            nums[i]%=k
            prefix[i]=(prefix[i-1]+nums[i])%k
            prefix[i]%=k
        mp[0].append(-1)
        for i,val in enumerate(prefix):
            mp[val].append(i)
        prev={}
        prev[0]=-1
        ans=0
        print(prefix)
        for i in range(n):
            if prefix[i] in prev:
                ans=max(ans,i-prev[prefix[i]])
            if prefix[i] not in prev:
                prev[prefix[i]]=i
        # print(-2%3)
            for j in range(i+1):
                #here we make 0 to i we make the current j to -ve val so the final 
                npref=((prefix[i]-(nums[j])+(-nums[j])%k))%k
                # print(j,npref)
                # print(mp[npref])
                idx=bisect.bisect_right(mp[npref],j-1)
                # print(idx)
                if len(mp[npref]):
                    if mp[npref][idx-1]<j:
                        ans=max(ans,i-mp[npref][0])
        return ans

