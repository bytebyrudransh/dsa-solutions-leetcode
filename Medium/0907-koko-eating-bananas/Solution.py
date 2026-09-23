class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=math.ceil(sum(piles)/h)
        high=max(piles)
        min_rate=high

        while low<=high:
            mid=(low+high)//2
            total=0

            for pile in piles:
                total+=math.ceil(pile/mid)
            if total>h:
                low=mid+1
            else:
                high=mid-1
                min_rate=min(min_rate,mid)
        return min_rate