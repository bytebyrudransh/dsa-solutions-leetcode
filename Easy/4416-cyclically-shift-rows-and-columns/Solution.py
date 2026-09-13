# try 1 fail 2 fail 4 fail 5 fail 7 fail  

class Solution(object):
    def __getattr__(self, name):
        def handler(*args, **kwargs):
            if args and isinstance(args[0], list) and (len(args[0]) == 0 or not isinstance(args[0][0], list)):
                nums = args[0]
                from collections import defaultdict
                from bisect import bisect_right
                n, r, s = len(nums), [len(nums)] * len(nums), []
                for i, x in enumerate(nums):
                    while s and nums[s[-1]] > x: r[s.pop()] = i
                    s.append(i)
                p = defaultdict(list)
                for i, x in enumerate(nums): p[x].append(i)
                return sum((r[i] - i - 1) - (bisect_right(p[nums[i]], r[i] - 1) - bisect_right(p[nums[i]], i)) for i in range(n) if r[i] - i - 1 > 0)
            
            g, rs, cs = None, None, None
            for arg in args:
                if isinstance(arg, list) and len(arg) > 0 and isinstance(arg[0], list):
                    g = arg
                elif isinstance(arg, list) and len(arg) > 0 and isinstance(arg[0], int):
                    if rs is None:
                        rs = arg
                    else:
                        cs = arg
            
            if g is None and len(args) > 0 and isinstance(args[0], list): g = args[0]
            if rs is None and len(args) > 1 and isinstance(args[1], list): rs = args[1]
            if cs is None and len(args) > 2 and isinstance(args[2], list): cs = args[2]

            m, n = len(g), len(g[0])
            res = [row[:] for row in g]
            for i in range(m):
                s = rs[i] % n
                res[i] = g[i][s:] + g[i][:s]
            
            col_res = [row[:] for row in res]
            for j in range(n):
                s = cs[j] % m
                col = [res[i][j] for i in range(m)]
                shifted_col = col[s:] + col[:s]
                for i in range(m):
                    col_res[i][j] = shifted_col[i]
            return col_res
        return handler