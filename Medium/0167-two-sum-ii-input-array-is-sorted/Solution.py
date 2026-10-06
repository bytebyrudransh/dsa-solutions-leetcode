class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pt1 = 0
        pt2 = len(numbers) - 1

        while pt1 < pt2:
            pst = numbers[pt1] + numbers[pt2]
            if pst == target:
                return [pt1+1, pt2+1] 
                #Adding 1 to each because problem statement specifies that
                #array 1-indexed array (first element's index is 1)
            elif pst > target:
                pt2 -= 1
            else:
                pt1 += 1