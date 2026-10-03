class Solution:
    def maxEarnings(self, itv: list[list[int]]) -> int:
        n = len(itv)
        itv.sort()
        mk = [-1]*n
        
        sl = SortedList()
        for i in range(n-1, -1, -1):
            l, r, _ = itv[i]
            j = sl.bisect_left((r, 0))
            if j < len(sl):  
                mk[i] = sl[j][1]
            sl.add((l, i))
        # print(itv)
        # print(mk)

        
        @cache
        def fn(i, f):
            if i >= n-1: return itv[i][2]
            res = 0
            if not f: 
                a = fn(i+1, f)
                if mk[i] != -1: 
                    k = mk[i]
                    d = itv[k][0]-itv[i][1]
                    b = fn(mk[i], 1) + itv[i][2] + d
                else: b = itv[i][2]
            else: 
                a = fn(i+1, f) + itv[i+1][0]-itv[i][0]
                if mk[i] != -1: 
                    k = mk[i]
                    d = itv[k][0]-itv[i][1]
                    b = fn(mk[i], f) + itv[i][2] + d
                else: b = itv[i][2]

            return max(a, b)
        res = fn(0, 0)
        return res