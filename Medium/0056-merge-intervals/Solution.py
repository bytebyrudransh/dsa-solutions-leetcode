class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        op = []

        for i in intervals:
            if not op or op[-1][1] < i[0]:
                op.append(i)
            else:
                op[-1][1] = max(op[-1][1], i[1])

        return op