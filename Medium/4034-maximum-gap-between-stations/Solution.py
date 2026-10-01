class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n = len(skill)
        earliest = []
        i = 0
        j = 0 
        while i<n:
            while skill[i]!= station[j]:
                j+=1
            earliest.append(j)
            i+=1
            j+=1
        #print(earliest)
        i = n-1
        j = len(station) -1
        latest = [None for i in range(n)]
        while i>=0:
            while skill[i]!= station[j]:
                j-=1
            latest[i] = j
            i-=1
            j-=1
        #print(latest)
        ans = 0
        for i in range(n-1):
            ans = max(ans, latest[i+1]-earliest[i])
        #print(ans)
        return ans


        