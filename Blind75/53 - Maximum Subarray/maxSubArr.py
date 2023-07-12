class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=0
        newSum=0
        if sum(nums)<0 and max(nums) < 0:
            return max(nums)
        for num in nums:
            if num > 0 or maxSum+num>0:
                maxSum=maxSum+num
                if maxSum > newSum:
                    newSum=maxSum
            else:
                maxSum=0
        return newSum
