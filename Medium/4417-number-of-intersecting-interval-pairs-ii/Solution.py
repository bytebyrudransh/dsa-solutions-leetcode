# time (n \log n) (I used my IDE for this code; writing code on that is easy then here )


from bisect import bisect_right


class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        starts = sorted(x[0] for x in intervals)

        total = n * (n - 1) // 2
        disjoint = 0
        for _, end in intervals:
            disjoint += n - bisect_right(starts, end)

        return total - disjoint