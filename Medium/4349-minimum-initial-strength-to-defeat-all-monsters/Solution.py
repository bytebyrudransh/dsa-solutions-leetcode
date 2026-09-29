class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:

        def is_valid(mid):
            strength = mid
            current_bonus = 0
            for i in range(len(monsters)):
                current_bonus += bonuses[i]
                total_strength = strength + current_bonus
                if monsters[i] > total_strength:
                    return False
                strength = max(strength - monsters[i], 0)
            return True

        bonuses = defaultdict(int)
        for l, r, v in boosts:
            bonuses[l] += v
            bonuses[r+1] -= v
        start, end = 0, sum(monsters)
        idx = 0
        while start <= end:
            mid = start + (end - start) // 2

            valid = is_valid(mid)
            if valid:
                idx = mid
                end = mid - 1
            else:
                start = mid + 1

        return idx