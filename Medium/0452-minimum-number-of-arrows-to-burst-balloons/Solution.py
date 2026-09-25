class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        x=points[0][1]
        cnt=1
        for i in range(1,len(points)):
            if points[i][0]<=x<=points[i][1]:
                continue
            else:
                x=points[i][1]
                cnt+=1
        return cnt