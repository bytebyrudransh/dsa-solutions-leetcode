# try 2 
class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        groups = [nums]
        power = [0] * 15
        
        for i in range(15):
            bit = 14 - i
            new_groups = []
            prefix_alive = True
            count = 0
            
            for g in groups:
                if prefix_alive:
                    g1 = [x for x in g if x & (1 << bit)]
                    g0 = [x for x in g if not (x & (1 << bit))]
                    
                    if g1:
                        new_groups.append(g1)
                        count += len(g1)
                    if g0:
                        new_groups.append(g0)
                        prefix_alive = False
                else:
                    new_groups.append(g)
                    
            groups = new_groups
            power[i] = count
            
        return power