class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        maxWaterArea=0
        while(end>start):
            maxWater = min(height[start],height[end])*(end-start)
            maxWaterArea = max(maxWater,maxWaterArea)
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return maxWaterArea
