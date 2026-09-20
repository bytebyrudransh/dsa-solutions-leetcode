class Solution:
    def countIntersectingIntervals(self, I):
        return sum(I[i][0] <= I[j][1] and I[j][0] <= I[i][1] for i in range(len(I)) for j in range(i + 1, len(I)))