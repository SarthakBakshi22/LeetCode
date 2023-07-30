class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum=0
        rightSum=sum(nums)
        
        for ind,num in enumerate(nums):
            rightSum -= num
            if leftSum==rightSum:
                return ind
            leftSum+=num
        return -1
