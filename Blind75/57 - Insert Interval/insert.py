class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left,right=[],[]
        for start in intervals:
            if start[1] < newInterval[0]:
                left.append(start)
            elif start[0] > newInterval[1]:
                right.append(start)
            else:
                newInterval=(min(start[0],newInterval[0]),max(start[1],newInterval[1]))
        return left+[newInterval] + right
