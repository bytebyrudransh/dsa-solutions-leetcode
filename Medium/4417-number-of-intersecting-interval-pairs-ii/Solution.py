class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        starts = sorted(start for start, _ in intervals)
        ends = sorted(end for _, end in intervals)

        intersections = 0
        ended = 0

        for processed, start in enumerate(starts):
            # Intervals ending at start still intersect
            while ended < len(ends) and ends[ended] < start:
                ended += 1

            # Previous intervals that are still active
            intersections += processed - ended

        return intersections